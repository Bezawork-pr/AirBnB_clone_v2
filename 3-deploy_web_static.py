#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack
plus
a Fabric script (based on the file 2-do_deploy_web_static.py) that
creates and distributes an archive to your web servers,
using the function deploy"""
from datetime import datetime
from fabric.api import local
from fabric.api import run
from fabric.api import put
from fabric.api import env
import os.path

env.hosts = ['34.202.158.152', '100.25.34.22']


def do_pack():
    """Generate a .tgz file"""
    try:
        current_time = datetime.now()
        format_date = current_time.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        path = "versions/web_static_{}.tgz".format(format_date)
        local("tar -cvzf {} web_static".format(path))
        return path
    except Exception as NotCreated:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        with_ext = archive_path.split("/")[-1]
        no_ext = with_ext.split(".")[0]
        put(archive_path, "/tmp/{}".format(with_ext))
        run("sudo rm -rf /data/web_static/releases/{}".format(no_ext))
        run("sudo mkdir -p /data/web_static/releases/{}".format(no_ext))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}".
            format(with_ext, no_ext))
        run("sudo rm /tmp/{}".format(with_ext))
        run("sudo mv /data/web_static/releases/{}/web_static/* \
             /data/web_static/releases/{}".format(no_ext, no_ext))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".
            format(no_ext))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{} \
                /data/web_static/current".format(no_ext))
        print("New version deployed!")
        return True
    except Exception as NotDeployed:
        return False


def deploy():
    create_tgz = do_pack()
    if create_tgz is None:
        return False
    return do_deploy(create_tgz)
