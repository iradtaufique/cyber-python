#!/usr/bin/python

import socket

# socket.AF_INET is used to connect for IPV4
# socket.SOCK_STREAM used for TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.0.159"
port = 5000

def portScanner(port):
	if sock.connect_ex((host, port)):
		print ('Port ' + str(port) + ' is Closed')
	else:
		print ('Port ' + str(port) + ' is Open')

portScanner(port)
