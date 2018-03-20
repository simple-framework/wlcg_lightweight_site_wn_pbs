#!/bin/bash

# move configuration files to the correct place
echo "Copying configuraiton files..."
cp /wn-config/wn-info.def /root/
cp /wn-config/users.conf /root/
cp /wn-config/groups.conf /root/
cp /wn-config/wn-list.conf /root/

# run YAIM
echo "Starting YAIM..."
/opt/glite/yaim/bin/yaim -c \
	-s /wn-config/wn-info.def \
	-n WN \
	-n TORQUE_client

# start daemons
service sshd start
service crond start
#service autofs start
