# Introduction

This folder contains the code and resources required to 
 - build a docker image for a worker node
 - run a container with the image of the worker node
 
The following sections describe how to get Docker Image for Worker Node and run it inside a docker.

# Pre-requisites

## Docker
You need to have docker installed on the machine.
You can go through the "Get Docker" section on the [Docker](https://www.docker.com) website to set it up, depending on your host platform(Windows/Mac/Linux).
For CentOS7, the following snippet will setup docker on your machine:
~~~
# install required packages
sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
# add stable repo
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
# Install docker-ce
sudo yum install docker-ce

# Start docker daemon
sudo systemctl start docker

# Verify installation by running a hello world container. See the output to see if the installation was a success.
sudo docker run hello-world
~~~
## permissions for init.sh
init.sh needs to be an executable:
` chmod "+x" {path_to_cern-lightweight-site}/WN/wn-config/init.sh`

# Configuration files/Additional Files and Folders
- Clone this repository
~~~
git clone https://github.com/maany/cern-lightweight-site
~~~
Next, 
 - Provide the YAIM configurations through the following files (located in ./wn-config/):
   - wn-info.def : main configuration file for **YAIM** 
   - users.conf
   - groups.conf
   - wn-list.conf : list the fully qualified domain name of the worker codes

Please note that the final direcrory structure inside the WN directory should look like:
```
.
├── Dockerfile
├── README.md
└── wn-config
    ├── groups.conf
    ├── init.sh
    ├── users.conf
    ├── wn-conf.def
    └── wn-list.conf
```
# Get the Docker Image 
 
 You can either download the docker image directly from [Docker Hub](https://hub.docker.com/r/maany/lightweight-site-wn/) or you can build the image on your machine using the Dockerfile included in the source code.
 
 ## Download Docker Image
 
` docker pull maany/lightweight-site-wn` 
 
 ## Build docker image
 If you want to build the docker image locally, you can build one from the Dockerfile included in the source code.
  - cd into the directory cern-lightweight-site/WN
  - build a docker image using the command
  `docker build -t lwwn .`
  
# Start a container
 
```
# please ensure that you specify the correct value for the placeholder {path_to_cern_lightweight_site_repo}
sudo docker run -d -it --name=wn --mount type=bind,source={path_to_cern_lightweight_site_repo}/WN/wn-config,target=/wn-config --net=host lwwn /bin/bash

```

# Some Helpful commands
~~~
# see all containers
docker ps -a
# open shell on running container
docker exec -it {name_of_the_conatiner} /bin/bash
~~~
