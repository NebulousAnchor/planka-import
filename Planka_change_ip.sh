#!/bin/bash

if [ $# -eq 0 ]
  then
    echo $'Usage: ./Planka_change_ip.sh <IP for Planka> \n eg. ./Planka_change_ip.sh 192.168.1.1'
    exit
fi

echo ':::Changing Base URL IP in Planka Docker Compose File:::'
sed -i 's/BASE_URL=http:\/\/.*/BASE_URL=http:\/\/'$1'\:3000/' docker-compose.yml

echo ':::Restarting Planka Container:::'
docker-compose up -d