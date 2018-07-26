#!/usr/bin/python

import socket
import time
import serial
import sys, os
import subprocess
#import pynmea2


ser = serial.Serial('/dev/ttyACM0',9600)

#UDP_IP = "10.0.0.2"
UDP_IP = "localhost"
UDP_PORT = 5005

outfile = open("./results_ping.txt", 'w')

last_gps = ''
while True:
    p = subprocess.Popen(['ping -c 1 -W 10 ' + UDP_IP], shell=True, stdout=subprocess.PIPE)
    while p.poll() == None:
    	data = ser.readline()
    	if (data.startswith("$GNGGA")):
      	    last_gps = data
    o, e = p.communicate()
    print o
    data = o
    output_str = "********\nReceived Message:" + data + '/' + last_gps
    print "********\nreceived message:", data, '/', last_gps
    outfile.write(output_str)
    outfile.flush()
    os.system('play system-ready.ogg -q -V0')
#       last_gps = pynmea2.parse(data)
