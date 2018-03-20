#!/bin/bash
sudo systemstl stop firewalld

sudo docker run -d \
	-it \
	--name lwwn \
	--net host \
	--mount type=bind,source="$(pwd)"/wn-config,target=/wn-config
	maany/lightweight-site-wn
	/bin/bash
