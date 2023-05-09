#!/usr/bin/python3
"""a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the
function do_deploy"""

from fabric.api import run, local, env, put
from datetime import datetime
import os

env.user = 'ubuntu'
env.hosts = ['35.174.209.69', '18.208.120.192']


def do_deploy(archive_path):
    """distributes an archive to your web servers,

    Args:
        archive_path:a compressed archive of the web_static folder.

    Return:
      if all operations have been done correctly, otherwise returns False
    """
    if not archive_path:
        return False

    result = put(archive_path, "/tmp/")
    if result.failed:
        return False

    filename = archive_path.split("/")[-1]
    folder_name = "/data/web_static/releases/" + filename.split(".")[0]

    run("sudo mkdir -p {}".format(folder_name))
    run("sudo tar -xzf /tmp/{} -C {}".format(filename, folder_name))
    run("sudo mv {}/web_static/* {}/".format(folder_name, folder_name))
    run("sudo rm -rf {}/web_static".format(folder_name))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s {} /data/web_static/current".format(folder_name))
    print('New version deployed!')

    return True
