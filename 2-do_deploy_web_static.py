#!/usr/bin/python3
"""a Fabric script (based on the file
1-pack_web_static.py) that distributes an
archive to your web servers,
using the function do_deploy:"""
from os.path import exists
from fabric.api import env
from fabric.api import put
from fabric.api import run
env.hosts = ['34.202.158.152', '100.25.34.22']


def do_deploy(archive_path):
    """distributes an archive to your web servers,
    using the function do_deploy"""
    if exists(archive_path) is False:
        return False
    f_we = archive_path.split("/")[-1]
    f_wo = f_we.split(".")[0]
    path = "/data/web_static/releases"
    path2 = "/data/web_static/current"
    try:
        put(archive_path, "/tmp/{}").format(f_we)
        run("rm -rf {}/{}/").format(path, f_wo)
        run("mkdir -p {}/{}/").format(path, f_wo)
        run("tar -xzf /tmp/{} -C {}/{}/").format(path, f_we, f_wo)
        run("rm /tmp/{}").format(f_we)
        run("mv {0}/{1}/web_static/* {0}/{1}/").format(path, f_wo)
        run("rm -rf {}/{}/web_static").format(path, f_wo)
        run("rm -rf {}").format(path2)
        run("ln -s {}/{}/ {}").format(path, f_wo, path2)
        return True
    except Exception as NotDeployed:
        return False
