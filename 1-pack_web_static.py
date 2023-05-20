#!/usr/bin/python3
""" This Fabric script distributes an archive to your
web servers, using the function do_deploy """
from fabric.api import *
from datetime import datetime


day = datetime.today().strftime("%Y%m%d")
time = datetime.now().strftime("%H%M%S")
day = day + time
archivePath = "versions/" + "web_static_" + day + ".tgz"


def do_pack():
    local('mkdir versions')
    local('tar -cvzf {} web_static'.format(archivePath))
