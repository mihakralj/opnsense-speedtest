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

arg='0'
if len(sys.argv)>1:
    arg=str(sys.argv[1])
if arg != '0':
    execute = ['/usr/local/opnsense/scripts/OPNsense/speedtest/speedtest.py', '--json', '--share', '--server', arg]
    #tt = subprocess.run(['/usr/local/opnsense/scripts/OPNsense/speedtest/speedtest.py', '--json', '--share', '--server', arg], stdout=subprocess.PIPE).stdout.decode('utf-8')
else:
    execute = ['/usr/local/opnsense/scripts/OPNsense/speedtest/speedtest.py', '--json', '--share']
    #tt= subprocess.run(['/usr/local/opnsense/scripts/OPNsense/speedtest/speedtest.py', '--json', '--share'], stdout=subprocess.PIPE).stdout.decode('utf-8')
try:
    tt = subprocess.run(execute, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True).stdout.decode('utf-8')
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
    ServerName = testjson['server']['sponsor']+', '+testjson['server']['name']
    Latency = testjson['ping']
    Jitter = 0
    DlSpeed = testjson['download']/1000000
    UlSpeed = testjson['upload']/1000000

    newrow = [Timestamp, ClientIp, ServerId, ServerName, Latency, Jitter, DlSpeed, UlSpeed] 

    f = open(csvfile, 'a')
    write = csv.writer(f) 
    write.writerow(newrow)
    print(tt, file=sys.stdout)

except subprocess.CalledProcessError as tt:
    print('speedtest.py '+str(tt.output)[2:], file=sys.stderr)
    sys.exit(0)


