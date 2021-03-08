#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

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
            uploadarray.append(float(row[6]))
            downloadarray.append(float(row[7]))
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
            'max': round(max(latencyarray),2)
            },
        'upload':  {
            'avg': round(statistics.mean(uploadarray),2),
            'min': round(min(uploadarray),2),
            'max': round(max(uploadarray),2)
            },
        'download': {
            'avg': round(statistics.mean(downloadarray),2),
            'min': round(min(downloadarray),2),
            'max': round(max(downloadarray),2)
        }
    }

    print(json.dumps(out))
    #print(max(timearray))

    #print("{'samples':", line, ", 'latency':", avglatency, ", 'upload':", avgul, ", 'download':", avgdl, "}")

finally:
    f.close()
