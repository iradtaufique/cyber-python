#! /usr/bin/python

from socket import *
import optparse
from threading import *


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

main()
