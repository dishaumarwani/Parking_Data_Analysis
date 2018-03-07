#!/usr/bin/env python
"""
    computes the total number of violations 
    for vehicles registered in
    the state of NY and all other vehicles
"""


import sys
import csv

def mapper():
        for line in sys.stdin:
            
            line = csv.reader([line], delimiter=',')
            line = list(line)[0]
            """
               This filters the state columns
               and outputs NY if state is NY 
               and Other for any other state
            """
            if (len(line) == 22):
                if(line[16] == 'NY'):
                    print('NY\t1')
                else:
                    print('Other\t1')

if __name__== "__main__":
    mapper()
