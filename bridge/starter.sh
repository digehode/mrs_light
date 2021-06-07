#!/bin/bash
for (( ; ; ))
do
    
    echo
    echo "--------------------------"
    echo " Mrs Light Bridge Started"
    echo "--------------------------"
    echo
    echo -n "IP: "
    ifconfig eth0|grep inet[^6]|cut -d " " -f 10
    python3 /root/control.py
    sleep 3

    clear
done
