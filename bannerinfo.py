#!/usr/bin/python

import socket

# function that return banner info
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return
    
def main():
    ip = input(f"Enter Target IP Address: ")
    for port in range(1,100):
        banner = retBanner(ip,port)
        if banner:
            print(f"[+] {ip}/{port} {banner}")

main()