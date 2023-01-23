#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy:"""
from datetime import datetime
from fabric.api import run
from fabric.api import put
from fabric.api import env
import os.path

env.hosts = ['34.202.158.152', '100.25.34.22']


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if os.path.exists(archive_path) is False:
        return False
    with_ext = archive_path.split("/")[-1]
    no_ext = with_ext.split(".")[0]
    put(archive_path, "/tmp/{}".format(with_ext))
    run("sudo rm -rf /data/web_static/releases/{}".format(no_ext))
    run("sudo mkdir -p /data/web_static/releases/{}".format(no_ext))
    run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(with_ext, no_ext))
    run("sudo rm /tmp/{}".format(with_ext))
    run("sudo mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}".format(no_ext, no_ext))
    run("sudo rm -rf /data/web_static/releases/{}/web_static".format(no_ext))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s /data/web_static/releases/{} /data/web_static/current".format(no_ext))
    print("New version deployed!")
    return True
