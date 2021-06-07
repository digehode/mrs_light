FROM ubuntu:cosmic
RUN ls
RUN apt-get update
RUN apt-get -y install netcat
RUN apt-get -y install e3
RUN apt-get -y install net-tools
RUN apt-get -y install sudo
RUN apt-get -y install iputils-ping


RUN apt-get -y install nmap 

RUN apt-get -y install tcpdump

RUN useradd -ms /bin/bash user
RUN echo user:resu|chpasswd
RUN mv /usr/sbin/tcpdump /bin/tcpdump
COPY starter.sh /root/
COPY hostExtras /tmp/hostExtras
RUN chmod u+x /root/starter.sh
CMD ["/root/starter.sh"]
