#!/usr/bin/python

import socket
import time


UDP_IP = "10.0.0.2"
UDP_PORT = 5005
MESSAGE = "KG5VBY "

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

count = 0
while True:
   print "message:", MESSAGE + ' ' + str(count)
   sock.sendto(MESSAGE + ' ' + str(count), (UDP_IP, UDP_PORT))
   time.sleep(10)
   count += 1
