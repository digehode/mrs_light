FROM ubuntu:cosmic
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata
RUN apt-get -y install apache2
RUN apt-get -y install libapache2-mod-php
RUN apt-get -y install net-tools
RUN apt-get -y install e3

COPY starter.sh /root/
RUN chmod u+x /root/starter.sh
COPY web /var/www/html/

RUN sed -i -e 's/AllowOverride None/AllowOverride All/g' /etc/apache2/apache2.conf
RUN sed -i -e 's/Require all denied/Require all granted/g' /etc/apache2/apache2.conf
RUN chown www-data /var/www/html/lights.dat

CMD ["/root/starter.sh"]
