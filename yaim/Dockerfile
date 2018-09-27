FROM cern/slc6-base
MAINTAINER Mayank Sharma (mayank.sharma@cern.ch)

####################
#  Misc packages
####################

RUN yum install -y \
	wget \
	openssh-clients \
	openssh-server

####################
#     UMD 4
####################

RUN yum install -y \
	yum-priorities

RUN yum install -y \
http://repository.egi.eu/sw/production/umd/4/sl6/x86_64/updates/umd-release-4.1.3-1.el6.noarch.rpm

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
	ca-policy-egi-core \
    emi-wn \
    emi-torque-client

# for compatibility between different versions...

RUN ln -s /var/spool/pbs /var/lib/torque

# Mount Volume for configuration parameters
VOLUME /wn-config

# init script on launch
#ENTRYPOINT ["/wn-config/init.sh"]
