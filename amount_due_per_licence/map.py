#!/usr/bin/env python
"""
    job that finds the total and average amount due in 
    open violations for each license type.
"""


import sys
import csv

def mapper():
    for line in sys.stdin:
        line = csv.reader([line], delimiter=',')
        line = list(line)[0]
        if(len(line) == 18):
            #Filter out the licence type and amount
            print('%s\t%s\t%s' % (str(line[2]), line[12],1))
if __name__== "__main__":
    mapper()
