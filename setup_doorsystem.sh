#!/bin/bash

if [ $(id -u) -ne 0 ]
        then echo Please run this script as root or using sudo!
        exit
fi

sudo apt update
sudo apt install nginx dehydrated

# Setup the Python scripts
cp metadoor/metadoor.service /etc/systemd/system/metadoor.service
cp metadoor/onsite_status.service /etc/systemd/system/onsite_status.service
cp metadoor/onsite_status.timer /etc/systemd/system/onsite_status.timer

systemctl daemon-reload
systemctl enable --now metadoor
systemctl enable --now onsite_status.timer

mkdir -p /var/www/metadoor/
cp -r metadoor/webpage /var/www/metadoor/
chown -R www-data:www-data /var/www/metadoor/

mkdir /tmpdoorstatus


if grep -Fxq "/tmpdoorstatus" /etc/fstab
then
        echo "tmpfs for doorstatus is already in fstab" 
else
        echo "tmpfs   /tmpdoorstatus         tmpfs   nodev,nosuid,size=1M          0  0" >> /etc/fstab
fi
sudo ln -s /tmpdoorstatus/status.json /var/www/metadoor/webpage/status.json
sudo ln -s  /tmpdoorstatus/doorstatus.json /var/www/metadoor/webpage/doorstatus.json


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
cp dehydrated/domains.txt /etc/dehydrated/
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


echo "Please reboot the system now to have the tmpfs ready!"
