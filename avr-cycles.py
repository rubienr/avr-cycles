#!/usr/bin/env python3

'''
    usage: avr-objcump -zS firmware.elf | python avr-cycles.py
    @author: raoul rubien 
    01/2016
'''

import sys
import csv
import json

scriptPath = sys.path[0]
config = json.load(open(scriptPath + "/avr-cycles.conf"))
tableFolder = sys.path[0] + "/" + config["instructionTablesFolder"] + "/"
table = config["instructionTable"]

reader = csv.reader(open(tableFolder + table, "r"))
dictionary = {}
for k,v in reader:
    if k in dictionary:
        dictionary[k] = dictionary[k] + "|" + v
    else:
        dictionary[k] = v
	

for line in sys.stdin:
    for k in dictionary.keys():
        line = line.replace("\t"+str.lower(k)+"\t", "\t[[%s -> %s]]\t" %(k, dictionary[k]))
    sys.stdout.write(line)
