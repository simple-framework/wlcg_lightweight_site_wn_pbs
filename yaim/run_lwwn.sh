#!/bin/bash

# parse arguments
for i in "$@"
do
case $i in
    --ip=*)
    IP="${i#*=}"
    shift # past argument=value
    ;;
    --host=*)
    HOST="${i#*=}"
    shift # past argument=value
    ;;
    --net=*)
    NET="${i#*=}"
    shift # past argument=value
    ;;
    --node=*)
    NODE="${i#*=}"
    shift # past argument=value
    ;;
    -h|--help)
    echo "Usage:"
    echo "run_lwwn.sh [--ip=<value>] [--hostname=<value>] [--node=<hostname>:<ip>] [--net=<value>] " 
esac
done

if [ -z "$IP" ]
then
    echo "Please specify the ip address for the workernode container." 
    exit 1
elif [ -z "$HOST" ]
then
    echo "Please specify the hostname for the workernode."
    exit 1
elif [ -z "$NET" ]
then
    echo "Please specify the name of the attachable docker overlay network that the container should connect to on startup."
    exit 1
elif [ -z $NODE ]
then
    echo "Please note that no node hostname:ip has been specified. Therefore this can potentially create some troubles when trying to communicate over the overlay network."
    exit 1
fi

echo  "Running docker run with this parameters:
	Hostname: $HOST
	IP ADDR: $IP
	Docker Network Name: $NET
	Node hostname and IP: $NODE
 	"
sudo systemctl stop firewalld
sudo docker build --rm  -t lwwn-umd4 .

sudo docker run -d \
        -itd \
        --privileged \
        --name $HOST \
        --net $NET \
        --ip $IP \
        --hostname $HOST \
        --add-host $NODE \
        --mount type=bind,source="$(pwd)"/wn-config,target=/wn-config \
        maany/lwwn-umd4 \
        /bin/bash
sudo docker exec -it lwwn-umd4 /wn-config/init.sh
