import nmap
import sys
from datetime import datetime

scanner= nmap.PortScanner()

targetHost= input("Enter teraget IP/hostname: ")
portRange= input("Enter port range: ")


try:
    startPort,endPort= map(int, portRange.split("-"))

    if startPort<1 or endPort>65535 or startPort >endPort:
        print("Invalid port range")
        sys.exit()
except ValueError:
    print("Invalid input")
    sys.exit()