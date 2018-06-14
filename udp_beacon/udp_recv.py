#!/usr/bin/python

import socket
import time
import serial
import sys, os
#import pynmea2


ser = serial.Serial('/dev/ttyACM0',9600)

UDP_IP = "10.0.0.2"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.setblocking(0)
sock.bind((UDP_IP, UDP_PORT))

outfile = open("./results.txt", 'w')

last_gps = ''
while True:
    try: 
       data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
       output_str = "Received Message:" + data + '/' + last_gps
       print "received message:", data, '/', last_gps
       outfile.write(output_str)
       outfile.flush()
       os.system('play system-ready.ogg -q -V0')
    except socket.error: pass
    data = ser.readline()
    if (data.startswith("$GNGGA")):
       last_gps = data
#       last_gps = pynmea2.parse(data)
