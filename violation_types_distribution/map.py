#!/usr/bin/env python
"""
    Distribution of the violation types, i.e., 
    for each violation code, the number of 
    violations that have this code
"""


import sys
import csv 

def mapper():
        for line in sys.stdin:
            
            line = csv.reader([line], delimiter=',')
            line = list(line)[0]
            """
                This filters the voilation_code columns
                and forms a tuple of voilation code.
                The violation code is the key and value is 1
            """
            if (len(line) == 22):
                print('%s\t%s' % (str(line[2]), 1))
		
if __name__== "__main__":
    mapper()
