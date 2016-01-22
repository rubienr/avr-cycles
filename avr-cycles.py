'''
    usage: avr-objcump -zS firmware.elf | python avr-cycles.py
    @author: raoul rubien 
    01/2016
'''

import sys
import csv

reader = csv.reader(open(sys.path[0]+"/tables/atmega-2560-instruction-2-cycles.csv", "r"))
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