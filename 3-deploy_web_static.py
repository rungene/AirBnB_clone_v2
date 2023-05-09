#!/usr/bin/python3
"""Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy:"""

from fabric.api import run, local, env, put
from datetime import datetime
import os


env.user = 'ubuntu'
env.hosts = ['35.174.209.69', '18.208.120.192']


def do_pack():
    """ generates a .tgz archive from the contents of the web_static folder"""
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")

        date = datetime.now().strftime('%Y%m%d%H%M%S')
        path_archive = "versions/web_static_{}.tgz".format(date)

        local("tar -cvzf {} web_static".format(path_archive))

        return path_archive

    except Exception:
        return None


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


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
