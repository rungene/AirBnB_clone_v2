#!/usr/bin/python3
"""
This Fabric script generates a .tgz archive from
the contents of the
web_static folder of the AirBnB Clone repo, using
the function do_pack."""


from fabric.api import local, env
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
