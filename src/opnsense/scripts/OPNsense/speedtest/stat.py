#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021 Miha Kralj
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.   You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.


import csv 
import json
import time
import statistics
import os.path
from os import path

fields = ['Timestamp', 'ClientIp', 'ServerId', 'ServerName', 'Latency', 'Jitter', 'DlSpeed', 'UlSpeed'] 
csvfile = "/usr/local/opnsense/scripts/OPNsense/speedtest/speedtest.csv"
latencyarray = []
downloadarray = []
uploadarray = []
timearray = []

p = not path.isfile(csvfile)
if p:
    f = open(csvfile, 'a')
    csv.writer(f).writerow(fields) 
    f.close()

try:
    f = open(csvfile, 'r')
    data = csv.reader(f)
    line = 0
    for row in data:
        if line > 0:
            timearray.append(row[0])
            latencyarray.append(float(row[4]))
            downloadarray.append(float(row[6]))
            uploadarray.append(float(row[7]))
        line += 1
    line -= 1
    if line==0:
        latencyarray = [0]
        downloadarray = [0]
        uploadarray = [0]
        timearray = [0]
    
    avglat = statistics.mean(latencyarray)
    avgdl = statistics.mean(downloadarray)
    avgul = statistics.mean(uploadarray)

    out = {
        'samples': line,
        'timestamp': {
            'oldest': min(timearray),
            'youngest': max(timearray)
        },
        'latency': {
            'avg': round(statistics.mean(latencyarray),2),
            'min': round(min(latencyarray),2),
            'max': round(max(latencyarray),2),
            'last': round(float(row[4]),2)
            },
        'upload':  {
            'avg': round(statistics.mean(uploadarray),2),
            'min': round(min(uploadarray),2),
            'max': round(max(uploadarray),2),
            'last': round(float(row[7]),2)
            },
        'download': {
            'avg': round(statistics.mean(downloadarray),2),
            'min': round(min(downloadarray),2),
            'max': round(max(downloadarray),2),
            'last': round(float(row[6]),2)
        }
    }

    print(json.dumps(out))
    #print(max(timearray))

    #print("{'samples':", line, ", 'latency':", avglatency, ", 'upload':", avgul, ", 'download':", avgdl, "}")

finally:
    f.close()
