#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy:"""
from datetime import datetime
from fabric.api import *


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
	try:
		no_ext, ext = archive_path.split(".")
		put(archive_path, "/tmp ")
		run("mkdir -p /data/web_static/releases/{}".format(no_ext))
		run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(archive_path, no_ext))
		run("rm /tmp/{}".format(archive_path))
		run("mv /data/web_static/releases/{}/web_static/* data/web_static/releases/{}".format)
		run("rm -rf /data/web_static/releases/{}/web_static".format(no_ext))
		run("rm -rf /data/web_static/current")
		run("ln -s /data/web_static/releases/{} /data/web_static/current".format(no_ext))
		return True
	except Exception as NotFound:
		return False
