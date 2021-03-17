#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021 Miha Kralj
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.   You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.


import sys
import csv 
import json
import time
import subprocess
import os.path
from os import path

arg=''
if len(sys.argv)>1:
    arg = str(sys.argv[1])
    arg = '-s'+str(sys.argv[1])
    if arg == '-s0':
        arg = ''

fields = ['Timestamp', 'ClientIp', 'ServerId', 'ServerName', 'Latency', 'Jitter', 'DlSpeed', 'UlSpeed'] 
csvfile = "/usr/local/opnsense/scripts/OPNsense/speedtest/speedtest.csv"

p = not path.isfile(csvfile)
if p:
    f = open(csvfile, 'a')
    csv.writer(f).writerow(fields) 
    f.close()

tt=subprocess.run(['/usr/local/opnsense/scripts/OPNsense/speedtest/speedtest', '--accept-license', '--accept-gdpr', '-fjson', arg], stdout=subprocess.PIPE).stdout.decode('utf-8')
testjson = json.loads(tt)

Timestamp = testjson['timestamp']
Timestamp = Timestamp[:10]+" "+Timestamp[11:19]
ClientIp = testjson['interface']['externalIp']
ServerId = testjson['server']['id']
ServerName = testjson['server']['name']+", "+testjson['server']['location']
Latency = testjson['ping']['latency']
Jitter = testjson['ping']['jitter']
DlSpeed = testjson['download']['bandwidth']/125000
UlSpeed = testjson['upload']['bandwidth']/125000

newrow = [Timestamp, ClientIp, ServerId, ServerName, Latency, Jitter, DlSpeed, UlSpeed] 

f = open(csvfile, 'a')
write = csv.writer(f) 
write.writerow(newrow)
print(tt, file=sys.stdout)