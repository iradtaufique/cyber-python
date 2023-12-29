#!/usr/bin/python

import socket
from termcolor import colored

# socket.AF_INET is used to connect for IPV4
# socket.SOCK_STREAM used for TCP

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Enter The Host IP Address to Scan: ")
#port = int(input("Enter The Port To Scan: "))



def portScanner(port):
	if sock.connect_ex((host, port)):
		print(colored(f"Port {port} is Closed", 'yellow'))
	else:
		print (colored(f"Port {port} is Open", 'green'))

# for loop that allow to scann more than one port at time
for port in range(5000,8000):
	portScanner(port)

