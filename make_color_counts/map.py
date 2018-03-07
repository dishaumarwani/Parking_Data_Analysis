#!/usr/bin/env python
"""
    distribution of terms for the Make and Color columns,
    i.e., for each value in those columns, how many times they appear in the column.
"""


import sys
#import numpy as np
import csv

def mapper():
        for line in sys.stdin:
            
            line = csv.reader([line], delimiter=',')
            line = list(line)[0]

            """
                The key will be NONE for black records,
                The a is appended to vehicle make so that it is printed 
                before color according to the requirement of the task 
                mentioned. The key values are in csv format.
            """
            if (len(line) == 22):
                if(line[20]== ''):
                    print('"a","vehicle_make", "NONE", "1"')
                else:
                    print('"a", "vehicle_make", "%s", "1"' % (line[20]))
                if(line[19]== ''):
                    print('"b", "vehicle_color", "NONE", "1"')
                else:
                    print('"b", "vehicle_color", "%s", "1"' % (line[19]))
          
if __name__=="__main__":
    mapper()
