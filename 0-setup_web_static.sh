#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Give ownership of the /data/ folder to the ubuntu user AND group 
sudo chown -R ubuntu:ubuntu /data/

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# update the package list
sudo apt-get -y  update

#Check if Nginx is installed
if ! [ -x "$(command -v nginx)" ]; then
  # install Nginx since it is not installed
  sudo apt-get -y install nginx
fi

# configure Nginx to serve web_static content
sudo sed -i "33i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# restart Nginx to apply changes
sudo service nginx restart 
