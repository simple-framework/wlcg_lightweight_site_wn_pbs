FROM cern/slc6-base
MAINTAINER Mayank Sharma (mayank.sharma@cern.ch)

####################
#  Misc packages
####################

RUN yum install -y \
	wget

####################
#     UMD 3
####################

RUN yum install -y \
	yum-priorities

RUN yum install -y \
http://repository.egi.eu/sw/production/umd/3/sl6/x86_64/updates/umd-release-3.14.4-1.el6.noarch.rpm

####################
#    Torque
####################

RUN wget -O /etc/yum.repos.d/EGI-third-party.repo \
http://repository.egi.eu/community/software/third.party.distribution/1.0/releases/repofiles/sl-6-x86_64.repo

#Let it override the unsupported Torque from EPEL:
RUN echo -e 'protect=1\npriority=1' >> /etc/yum.repos.d/EGI-third-party.repo

###################
#  Configuration
################### 

RUN yum -y install \ 
	lcg-CA \
        emi-wn \
        emi-torque-client

# for compatibility between different versions...

RUN ln -s /var/spool/pbs /var/lib/torque

# Mount Volume for configuration parameters
VOLUME /wn-config

# init script on launch
# TODO script should be packaged within the image, using on mount point only for development purposes
#ENTRYPOINT ["/wn-config/init.sh"]
