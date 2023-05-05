#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

sudo echo "<!DOCTYPE html>
<html>
<head>
  <title>NGINX Test Page</title>
</head>
<body>
  <h1>NGIX test page.</h1>
  <p>Served from Nginx, configuration is working!</p>
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Give ownership of the /data/ folder to the ubuntu user AND group 
chown -R ubuntu:ubuntu /data/

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
ln -sf /data/web_static/releases/test/ /data/web_static/current

# update the package list
sudo apt-get -y  update

#Check if Nginx is installed
if ! [ -x "$(command -v nginx)" ]; then
  # install Nginx since it is not installed
  sudo apt-get -y install nginx
fi

# configure Nginx to serve web_static content
sudo sed -i "26i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# restart Nginx to apply changes
sudo service nginx restart 
