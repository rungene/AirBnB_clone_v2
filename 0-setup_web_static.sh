#!/usr/bin/env bash
# This script sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/ /data/web_static/ /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test
content="
<html>
<h1> HELLO. THIS IS MY WEBSITE </h1>
</html>"
echo $content | sudo tee /data/web_static/releases/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
config="
http {
	server {
		listen 80;
		server_name https://www.dh4nn.tech http://www.dh4nn.tech http://dh4nn.tech;
		root /data/web_static/current/;

		location /hbnb_static {
                	alias /data/web_static/current/;
        	}
	}
}
events {}"
echo $config | sudo tee /etc/nginx/nginx.conf
sudo service nginx restart
