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
array = []

p = not path.isfile(csvfile)
if p:
    f = open(csvfile, 'a')
    csv.writer(f).writerow(fields) 
    f.close()

table_head = """<table id="grid-log" class="table table-condensed table-hover table-striped table-responsive bootgrid-table">
<thead><tr>
<th data-column-id="Timestamp" class="text-left" style="width:11em;"></th>
<th data-column-id="ClientIp" class="text-left" style="width:2em;"></th>
<th data-column-id="ServerId" class="text-left" style="width:11em;"></th>
<th data-column-id="ServerName" class="text-left" style="width:10em;"></th>
<th data-column-id="Latency" class="text-left" style="width:10em;"></th>
<th data-column-id="Jitter" class="text-left" style="width:10em;"></th>
<th data-column-id="DlSpeed" class="text-left" style="width:10em;"></th>
<th data-column-id="UlSpeed" class="text-left" style="width:10em;"></th>
</tr></thead><tbody>"""
table_tail = "</tbody></table>"

try:
    f = open(csvfile, 'r')
    data = csv.reader(f)
    header = next(data)
    #print(json.dumps(header))
    for row in data:
        array.append(row)
    array=sorted(array, reverse=True)
    #for row in array:
     #   print(json.dumps(row))
    print(json.dumps(array))
        #print("<tr><td class=\"text-left\" style=\"\">"+row[0]+"</td>")
        #print("<td class=\"text-left\" style=\"\">"+row[1]+"</td>")
        #print("<td class=\"text-left\" style=\"\">"+row[2]+"</td>")
        #print("<td class=\"text-left\" style=\"\">"+row[3]+"</td>")
        #print("<td class=\"text-left\" style=\"\">"+row[4]+"</td>")
        #print("<td class=\"text-left\" style=\"\">"+row[5]+"</td>")
        #print("<td class=\"text-left\" style=\"\">"+row[6]+"</td>")
        #print("<td class=\"text-left\" style=\"\">"+row[7]+"</td></tr>")
    #print(table_tail)

finally:
    f.close()

