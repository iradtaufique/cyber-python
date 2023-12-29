#! /usr/bin/python

from socket import *
import optparse
from threading import *
from  termcolor import colored

def connScan(tgtHost, tgtPort):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((tgtHost, tgtPort))
		print(colored(f"Port {tgtPort} is Open", 'green'))
	except:
		print(colored(f"Port {tgtPort} is Closed", 'yellow'))

	finally:
		sock.close()

def portScan(tgtHost, tgtPorts):
	try:
		tgtIp = gethostbyname(tgtHost)
	except:
		print(f"Unknown Host {tgtHost}")

	try:
		tgtName = gethostbyaddr(tgtIp)
		print(f"Scan Results for: {tgtName[0]}")
	except:
		print(f"Scan Result for: {tgtIp}")

	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		t.start()


def main():
	parser = optparse.OptionParser("Usage of Program: " + "-H <Target Host> -p <target Port>")
	parser.add_option("-H", dest="tgtHost", type="string", help="Specify Target Host")
	parser.add_option("-p", dest="tgtPort", type="string", help="Specify Target Ports")
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print( parser.usage)
		exit(0)
	portScan(tgtHost, tgtPorts)
main()
