FROM ubuntu:cosmic
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata
RUN apt-get -y install net-tools
RUN apt-get -y install e3
RUN apt-get -y install python3 python3-requests
COPY starter.sh /root/
COPY control.py /root/
RUN chmod u+x /root/starter.sh

CMD ["/root/starter.sh"]
