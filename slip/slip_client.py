#!/usr/bin/sh

slattach -v -s 9600 /dev/ttyUSB0 &
ifconfig sl0 10.0.0.2 dstaddr 10.0.0.1 netmask 255.255.255.0
