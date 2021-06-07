#!/bin/bash
/etc/init.d/apache2 start

for (( ; ; ))
do
    
    echo
    echo "--------------------------"
    echo " Mrs Light Server Started"
    echo "--------------------------"
    echo
    echo -n "IP: "
    ifconfig eth0|grep inet[^6]|cut -d " " -f 10
    echo "-- Access --"
    tail /var/log/apache2/access.log
    echo "-- Error --"
    tail /var/log/apache2/error.log

    sleep 3

    clear
done
