#!/usr/bin/env python3

import os
import sys
import shutil
import click
import yaml
from myppa import __version__
from myppa.utils import *
from myppa.package import Package
import sqlite3
import jenkins

@click.group()
@click.version_option(__version__)
@click.option("--http-proxy", help="HTTP proxy URL, e.g. http://user:password@127.0.0.1:3128")
@click.pass_context
def cli(ctx, http_proxy):
    ctx.obj["http-proxy"] = http_proxy

@cli.command()
def clean():
    """Clean packages.db"""
    cwd = ensure_cwd()
    cache_dir = os.path.join(cwd, "cache")
    if not click.confirm("Erase cache/ directory?"):
        return
    for filename in os.listdir(cache_dir):
        if filename == ".placeholder":
            continue
        fullpath = os.path.join(cache_dir, filename)
        if os.path.isdir(fullpath):
            shutil.rmtree(fullpath)
        else:
            os.remove(fullpath)

@cli.command()
def list():
    """List all packages in packages.db"""
    conn = sqlite3.connect(get_packages_db())
    c = conn.cursor()
    print("Packages with fixed versions")
    for row in c.execute("SELECT name, version from package WHERE NOT version_is_computed ORDER BY name"):
        print(row[0], row[1])
    print("Packages with version computed upon build")
    for row in c.execute("SELECT name, version from package WHERE version_is_computed ORDER BY name"):
        print(row[0], row[1])
    conn.close()

@cli.command()
def update():
    """Update packages.db according to specs"""
    specs = []
    for root, dirs, files in os.walk(get_specs_dir()):
        for filename in files:
            if filename.endswith(".yaml") or filename.endswith(".yml"):
                specs.append(os.path.join(root, filename))
    click.echo("Total {} spec files found".format(len(specs)))
    if os.path.exists(get_packages_db()):
        os.remove(get_packages_db())
    conn = sqlite3.connect(get_packages_db())
    c = conn.cursor()
    c.execute("CREATE TABLE package (name TEXT, version_is_computed INTEGER, version TEXT, description TEXT)")
    for spec in specs:
        click.echo("Processing '{}'".format(spec))
        with open(spec, 'r') as f:
            for document in yaml.load_all(f):
                for name, package in document.items():
                    if not name.startswith("package-"):
                        continue
                    pkg = Package(package)
                    pkg.validate()
                    pkg.persist(conn)
    conn.commit()
    conn.close()

@cli.command()
@click.argument("package")
@click.option("--format", "-f",
        type=click.Choice(supported_formats()),
        default=supported_formats()[0])
@click.option("--resolve", "-r", required=False)
@click.option("--distribution", "-d", required=False,
        type=click.Choice(supported_distributions()),
        default=supported_distributions()[0])
@click.option("--architecture", "-a", required=False,
        type=click.Choice(supported_architectures()),
        default=supported_architectures()[0])
def show(package, format, resolve, distribution, architecture):
    """Print spec of the given package"""
    dist, codename = parse_distribution(distribution)
    pkg = get_package(package)
    description = pkg.resolve(dist, codename, architecture) if resolve else pkg.description()
    click.echo(format_object(description, format))

@cli.command()
@click.argument("package")
@click.option("--distribution", "-d",
        type=click.Choice(supported_distributions()),
        default=supported_distributions()[0])
@click.option("--architecture", "-a",
        type=click.Choice(supported_architectures()),
        default=supported_architectures()[0])
@click.pass_context
def script(ctx, package, distribution, architecture):
    """Print build.sh for the given package"""
    click.echo(get_script(ctx.obj["http-proxy"], package, distribution, architecture))

@cli.command()
@click.argument("package")
@click.option("--distribution", "-d",
        type=click.Choice(supported_distributions()),
        default=supported_distributions()[0])
@click.option("--architecture", "-a",
        type=click.Choice(supported_architectures()),
        default=supported_architectures()[0])
@click.option("--upload-to",
        type=click.Choice(supported_deb_providers()),
        default=supported_deb_providers()[0])
@click.option("--bintray-login", required=False)
@click.option("--bintray-token", required=False)
@click.pass_context
def build(ctx, package, distribution, architecture, upload_to, bintray_login, bintray_token):
    """Build package"""
    run_builder(ctx.obj["http-proxy"], package, distribution, architecture, upload_to, bintray_login, bintray_token)

@cli.command()
@click.pass_context
@click.option("--upload-to",
        type=click.Choice(supported_deb_providers()),
        default=supported_deb_providers()[0])
@click.option("--bintray-login", required=False)
@click.option("--bintray-token", required=False)
def buildall(ctx, upload_to, bintray_login, bintray_token):
    """Build all packages from the database"""
    conn = sqlite3.connect(get_packages_db())
    packagelist = []
    c = conn.cursor()
    for row in c.execute("SELECT name, version from package ORDER BY name"):
        packagelist.append(row)
    conn.close()
    for arch in supported_architectures():
        for distr in supported_distributions(with_aliases=False):
            for namever in packagelist:
                run_builder(ctx.obj["http-proxy"], "@".join(namever), distr, arch, upload_to, bintray_login, bintray_token)

@cli.command()
def info():
    """Print a list of supported features"""
    print("Architectures:")
    for arch in supported_architectures():
        print("-", arch)
    print("Distributions:")
    for dist in supported_distributions(with_aliases=False):
        print("-", dist)
    print("DEB providers:")
    for prov in supported_deb_providers():
        print("-", prov)

@cli.command(name="setup-jenkins")
@click.pass_context
@click.argument("host")
@click.option("--user", required=False)
@click.option("--token", required=False)
@click.option("--secret", required=False)
def setup_jenkins(ctx, host, user, token, secret):
    """Configure Jenkins CI to build packages.db"""
    j = jenkins.Jenkins(host, username=user, password=token)
    print("Connected to Jenkins at {} as {}".format(host, user))
    for job in j.get_all_jobs():
        if job['fullname'].startswith('myppa'):
            print("Jenkins is already configured for MyPPA")
            return 1
    conn = sqlite3.connect(get_packages_db())
    packagelist = []
    c = conn.cursor()
    for row in c.execute("SELECT name, version from package ORDER BY name"):
        packagelist.append(row)
    conn.close()
    for package in packagelist:
        pkg = get_package("@".join(package))
        for arch in supported_architectures():
            for dist in supported_distributions(with_aliases=False):
                dist, codename = parse_distribution(dist)
                resolved_pkg = pkg.resolve(dist, codename, arch)
                folder = resolved_pkg.get('jenkins-folder') or resolved_pkg['name']
                full_path = [
                    "myppa",
                    folder,
                    '-'.join((dist, codename)),
                    arch,
                    '-'.join((resolved_pkg['name'], resolved_pkg['version']))
                ]
                for i in range(1, len(full_path)):
                    ifolder = "/".join(full_path[:i])
                    if not j.job_exists(ifolder):
                        j.create_job(ifolder, JENKINS_FOLDER_CONFIG_XML)
                joburl = "/".join(full_path)
                configxml = get_jenkins_config(ctx.obj["http-proxy"], pkg, dist, arch)
                j.create_job(joburl, configxml)
                print("Job {} created".format(joburl))

def main():
    return cli(obj={})

if __name__ == "__main__":
    sys.exit(main())
