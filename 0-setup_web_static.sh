#!/usr/bin/env bash
#  a Bash script that sets up your web servers for the deployment of web_static
apt-get update -y
apt-get install -y nginx

sudo echo "Hello World!" |  /var/www/html/index.nginx-debian.html
sed -i "/server_name _;/ a\\\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default
sudo vim /var/www/html/error-404.html
echo "Ceci n'est pas une page" > /var/www/html/error-404.html
sed -i "/http {/ a\\\terror_page 404 /error-404.html;" /etc/nginx/nginx.conf
sed -i  "/server {/a\\\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i "54i \\\tlocation /htbn_static {\n\t\talias /data/web_static/current/;\n\t\tindex index.html index.htm;}" /etc/nginx/sites-available/default 
sudo service nginx restart
