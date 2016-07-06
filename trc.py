#!/usr/bin/python
#///////////bANNER
"""
          __        _______ _     ____ ___  __  __ _____ 
          \ \      / / ____| |   / ___/ _ \|  \/  | ____|
           \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|  
            \ V  V / | |___| |__| |__| |_| | |  | | |___  _   _   _ 
             \_/\_/  |_____|_____\____\___/|_|  |_|_____|(_| |_| |_)
                                               
                        Script Crearor: 
     _   _    _____ _    ____    _____  ___     ___    _   _    _    
    | | / \  |  ___/ \  |  _ \  |_   _|/ \ \   / / \  | \ | |  / \   
 _  | |/ _ \ | |_ / _ \ | |_) |   | | / _ \ \ / / _ \ |  \| | / _ \  
| |_| / ___ \|  _/ ___ \|  _ <    | |/ ___ \ V / ___ \| |\  |/ ___ \ 
 \___/_/   \_\_|/_/   \_\_| \_\   |_/_/   \_\_/_/   \_\_| \_/_/   \_\
                                                                     
Tell:  +989170118221   		  Mail: PowerInfoSSL@Gmail.com
"""
##
import sys,os
os.system('clear')
from scapy.all import *
try:
	addr=sys.argv[1]
except:
	print 'Pleas Enter Address.'
	exit(0)
def ff(add,ttl=128):
	e=IP(dst=add)/ICMP()
	ee=sr1(e,timeout=1)
	if ee[IP].src!=add:
		os.system('clear')
		print 'Destination Is not Accessible.'
		os._exit(0)
	u=IP(dst=add,ttl=ttl)/ICMP()
	uu=sr1(u,timeout=1)
	return uu
def pr(txt):
	print '\n'+txt+'\n'

print 'Your Address is %s' % addr
pr('\n\n[+]Get Information From Your Target\n')
cu=0
try:
	ss=ff(addr)
	#cu=ss[IP].ttl
except:
	print 'You Entred Bad IP address.\n'
	exit(0)
y=[]
os.system('clear')

while True:
	cu=cu+1
	b=ff(addr,cu)
	if b[IP].src==addr:
		print 'OK....................................................'
		break
	else:
		y.append(b[IP].src)
os.system('reset')
tt=0
for t in y:
	tt=tt+1
	ll=15-len(t)
	print '[+] '+t+' '+('*'*(tt+ll))+' '*((15-tt)*2)+('*'*(tt+ll))

