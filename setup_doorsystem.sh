#!/bin/bash

if [ $(id -u) -ne 0 ]
        then echo Please run this script as root or using sudo!
        exit
fi

sudo apt update
sudo apt install nginx

git clone git@github.com:Metalab/metadoor.git
cd metadoor

# setup the Python script

cp metadoor/metadoor.service /etc/systemd/system/metadoor.service
systemctl daemon-reload
systemctl enable --now metadoor

mkdir -p /var/www/metadoor/
cp -r metadoor/webpage /var/www/metadoor/

# Setup the nginx config

cp nginx/eingang.metalab.at /etc/nginx/sites-available/
cp -r nginx/common /etc/nginx

mkdir /etc/nginx/dhparam/
curl https://ssl-config.mozilla.org/ffdhe2048.txt > /etc/nginx/dhparam/dhparam.pem

mdkir /var/www/empty

dehydrated --register --accept-terms

adduser --system --no-create-home --home /var/lib/dehydrated \
        --shell /usr/bin/nologin --disabled-login \
        --gecos "dehydrated ACME client,,," --group dehydrated
chown -R dehydrated: /var/lib/dehydrated

mkdir /var/www/dehydrated
chown dehydrated:www-data /var/www/dehydrated
chmod u=rwx,go=rx /var/www/dehydrated

cp dehydrated/dehydrated.config /etc/dehydrated/config
cp dehydrated/dehydrated.service /etc/systemd/system/dehydrated.service

systemctl daemon-reload
systemctl start dehydrated

# set timer
cp dehydrated/dehydrated.timer /etc/systemd/system/dehydrated.timer
systemctl daemon-reload
systemctl enable dehydrated.timer
systemctl start dehydrated.timer


# create symlink to enable webpage
ln -s /etc/nginx/sites-available/nginx/eingang.metalab.at /etc/nginx/sites-enabled/nginx/eingang.metalab.at

# check nginx config and enable it
nginx -t
nginx -s reload