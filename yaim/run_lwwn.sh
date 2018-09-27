#!/bin/bash
ipcontainer=$1
hostnamecontainer=$2
ipcream=$3
hostnamecream=$4
netname=$5

sudo systemctl stop firewalld
sudo docker build --rm  -t lwwn-umd4 .
sudo docker run -d \
        -itd \
        --privileged \
        --name $hostnamecontainer \
        --net $netname \
        --ip $ipcontainer \
        --hostname $hostnamecontainer \
        --add-host $hostnamecream:$ipcream \
        --mount type=bind,source="$(pwd)"/wn-config,target=/wn-config \
        maany/lwwn-umd4 \
        /bin/bash

#sudo docker exec -it lwwn-umd4 /wn-config/init.sh
