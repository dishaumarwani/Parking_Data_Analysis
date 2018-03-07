#!/usr/bin/env python
"""
    finds the vehicle that has had the greatest number of violations
    (assuming that plate_id and registration_state uniquely identify a vehicle).
"""


import sys
import csv

def mapper():
        for line in sys.stdin:
           
            line = csv.reader([line], delimiter=',')
            line = list(line)[0]
            """
                This filters plateid and registration columns
                which are used to identify a vehicle
            """
            if (len(line) == 22):
                print('%s, %s\t%s'% (line[14], line[16],1))

if __name__== "__main__":
    mapper()
