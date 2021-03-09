#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv 
import json
import time
import subprocess
import os.path
from os import path

arg=''
if len(sys.argv)>1:
    tt = subprocess.run(['/usr/local/opnsense/scripts/OPNsense/speedtest/speedtest.py', '--json', '--share', '--server', str(sys.argv[1])], stdout=subprocess.PIPE).stdout.decode('utf-8')
else:
    tt= subprocess.run(['/usr/local/opnsense/scripts/OPNsense/speedtest/speedtest.py', '--json', '--share'], stdout=subprocess.PIPE).stdout.decode('utf-8')

testjson = json.loads(tt)
fields = ['Timestamp', 'ClientIp', 'ServerId', 'ServerName', 'Latency', 'Jitter', 'DlSpeed', 'UlSpeed'] 
csvfile = "/usr/local/opnsense/scripts/OPNsense/speedtest/speedtest.csv"

p = not path.isfile(csvfile)
if p:
    f = open(csvfile, 'a')
    csv.writer(f).writerow(fields) 
    f.close()

Timestamp = testjson['timestamp']
Timestamp = Timestamp[:10]+" "+Timestamp[11:19]
ClientIp = testjson['client']['ip']
ServerId = testjson['server']['id']
ServerName = testjson['server']['sponsor']
Latency = testjson['ping']
Jitter = 0
DlSpeed = testjson['download']/1000000
UlSpeed = testjson['upload']/1000000

newrow = [Timestamp, ClientIp, ServerId, ServerName, Latency, Jitter, DlSpeed, UlSpeed] 

f = open(csvfile, 'a')
write = csv.writer(f) 
write.writerow(newrow)

print(tt, file=sys.stdout)