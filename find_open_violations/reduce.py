#!/usr/bin/env python


from operator import itemgetter
import sys

word = None
count = 0
current_word = None
current_count = 0
current_issue_date = None
current_precint = None
current_plate_id = None
current_vio_code = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    #Seperate the key and values by tab space
    line = list(line.strip().split('\t'))
    """
        Open_parking.csv file has 18 columns and
        parking_violations.csv has 22 columns.
        So, after identifying the file the code
        parses the line into key and value
     """
    if(len(line)==5):
        summons_number, plate_id, violation_precinct, issue_date, violation_code = line
    else:
        try:
            summons_number, plate_id, violation_precinct, issue_date = line
            violation_code = None
        except:
            #In case of blank records
            pass

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == summons_number:
        count += 1
    else:
        #print only if count is 1 i.e. the record is only in parking violations
        #and current_vio_code helps to identify if the record is from parking-violations
        #or open-violations
        if(count == 1 and current_vio_code != None):
            print('%s\t%s, %s, %s, %s' % (current_word, current_plate_id, current_precint, current_vio_code, current_issue_date))
        current_word = summons_number
        count = 1
        current_issue_date = issue_date
        current_precint = violation_precinct
        current_plate_id = plate_id
        current_vio_code = violation_code

# do not forget to output the last word if needed!
if current_word:
    if (count == 1 and current_vio_code != None):
    	print('%s\t%s, %s, %s, %s' % (summons_number, plate_id, violation_precinct, violation_code, issue_date) )
