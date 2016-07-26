#!/usr/bin/env python3

'''
    usage: avr-objcump -zS firmware.elf | python avr-cycles.py
    usage: avr-objcump -zS firmware.elf | python avr-cycles.py --mmcu=<mmcu>
    @author: raoul rubien 
    07/2016
'''

import sys
import csv
import json

scriptPath = sys.path[0]
config = json.load(open(scriptPath + "/avr-cycles.conf"))
tableFolder = sys.path[0] + "/" + config["instructionTablesFolder"] + "/"
table = config["instructionTable"]

# overwrite default value if specified per cli: --mmcu=newMcu
if len(sys.argv) == 2:
    mmcu = sys.argv[1]
    print("1 mmcu: %s" % mmcu)
    if "-mmcu=" in mmcu:
        mmcu = mmcu.replace("-mmcu=", "")
    print("mmcu: %s" % mmcu)
    table = config[mmcu]

# read lookup table
reader = csv.reader(open(tableFolder + table, "r"))
dictionary = {}
for k,v in reader:
    if k in dictionary:
        dictionary[k] = dictionary[k] + "|" + v
    else:
        dictionary[k] = v
	
# translate stdin
for line in sys.stdin:
    for k in dictionary.keys():
        line = line.replace("\t"+str.lower(k)+"\t", "\t[[%s -> %s]]\t" %(k, dictionary[k]))
    sys.stdout.write(line)
