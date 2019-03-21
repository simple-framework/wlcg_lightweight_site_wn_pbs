#!/bin/bash

# move configuration files to the correct place
echo "Copying configuraiton files..."
cp /etc/simple_grid/config/wn-info.def /root/
cp /etc/simple_grid/config/users.conf /root/
cp /etc/simple_grid/config/groups.conf /root/
cp /etc/simple_grid/config/wn-list.conf /root/

service rsyslog start

# run YAIM
echo "Starting YAIM..."
/opt/glite/yaim/bin/yaim -c \
	-s /etc/simple_grid/config/wn-info.def \
	-n WN \
	-n TORQUE_client

# start daemons
service sshd start
service crond start

