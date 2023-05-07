#!/usr/bin/python3
"""a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the
function do_deploy"""

from fabric.api import run, local, env, put
from fabric.contrib.files import append
from datetime import datetime
from os.path import exists


env.hosts = ['35.174.209.69, 18.208.120.192']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """distributes an archive to your web servers,

    Args:
        archive_path:a compressed archive of the web_static folder.

    Return:
      if all operations have been done correctly, otherwise returns False
    """
    if not archive_path:
        return False
