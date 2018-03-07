#!/usr/bin/env python
"""
    Finding the voilations that are open.
    This is basically a right out join for
    parking-violations.csv and open-violations.csv
"""


import sys
import csv

def mapper():
    for line in sys.stdin:
        line = csv.reader([line], delimiter=',')	
        line = list(line)[0]            
        """
           Open_parking.csv file has 18 columns and 
           parking_violations.csv has 22 columns.
           So, after identifying the file the code
            parses the line into key and value
        """
        if (len(line) == 22):
            #Filtering out summons_number, plate_id, violation_precinct, violation_code, issue_date
            print('%s\t%s\t%s\t%s\t%s' % (line[0], line[14], line[6], line[1], line[2]))
        else:
            # summons_number, plate_id, violation_precinct, issue_date
            print('%s\t%s\t%s\t%s' % (line[0], line[1], line[5], line[9]))
           
if __name__== "__main__":
    mapper()
