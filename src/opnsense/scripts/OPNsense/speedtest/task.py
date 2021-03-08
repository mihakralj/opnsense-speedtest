#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import csv 
import json
import time
import subprocess
import os.path
from os import path

fields = ['Timestamp', 'ClientIp', 'ServerId', 'ServerName', 'Latency', 'Jitter', 'DlSpeed', 'UlSpeed'] 
csvfile = "/usr/local/opnsense/scripts/OPNsense/speedtest/speedtest.csv"

p = not path.isfile(csvfile)
if p:
    f = open(csvfile, 'a')
    csv.writer(f).writerow(fields) 
    f.close()

testjson = json.loads(subprocess.run(['/usr/local/opnsense/scripts/OPNsense/speedtest/speedtest', '--accept-license', '--accept-gdpr', '-fjson'], stdout=subprocess.PIPE).stdout.decode('utf-8'))

Timestamp = testjson['timestamp']
Timestamp = Timestamp[:10]+" "+Timestamp[11:19]
ClientIp = testjson['interface']['externalIp']
ServerId = testjson['server']['id']
ServerName = testjson['server']['name']
Latency = testjson['ping']['latency']
Jitter = testjson['ping']['jitter']
DlSpeed = testjson['download']['bandwidth']/125000
UlSpeed = testjson['upload']['bandwidth']/125000

newrow = [Timestamp, ClientIp, ServerId, ServerName, Latency, Jitter, DlSpeed, UlSpeed] 

f = open(csvfile, 'a')
write = csv.writer(f) 
write.writerow(newrow) 
