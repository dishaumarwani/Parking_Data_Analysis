#!/usr/bin/env python

"""
    The algorithm calculates the number of
    weekends and weekdays for the month of
    March in 2016. Then, it maintains an 
    count of Weekday or Weekend with respect to each key
    In the end, it just divides the count by total no. of
    weekdays and weekends in that Month and prints it to console.
"""

from operator import itemgetter
import sys
from datetime import datetime,date,timedelta
import csv 


#Function to find number of weekends and weekdays between two dates
def num_days(start_date, end_date):
    month, day, year = start_date.split("/")
    from_date = date(int(year), int(month), int(day))
    month, day, year = end_date.split("/")
    to_date = date(int(year), int(month), int(day))
    daygenerator = (from_date + timedelta(x + 1) for x in range((to_date - from_date).days))
    weekdays = sum(1 for day in daygenerator if datetime.weekday(day) < 5)
    daygenerator = (from_date + timedelta(x + 1) for x in range((to_date - from_date).days))
    weekends = sum(1 for day in daygenerator if datetime.weekday(day) >4)
    return weekdays, weekends

current_violation_code = None
current_day_type = None
current_weekday = 0
current_weekend = 0
# input comes from STDIN
weekdays, weekends = num_days('3/1/2016', '4/1/2016')
for line in sys.stdin:
    
    # remove leading and trailing whitespace
    line = line.strip()
    
    line = line.split("\t")

    violation_code, day_type = line

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if (current_violation_code == violation_code):
        if(day_type.strip() == "Weekend"):
            current_weekend += 1
        elif(day_type.strip() == "Weekday"):
            current_weekday += 1
    else:
        if(current_violation_code):
            try:
                avg_weekend = current_weekend/weekends
                avg_weekday = current_weekday/weekdays
            except:
                avg_weekend = current_weekend
                avg_weekday = current_weekday
            # write result to STDOUT
            print ('%s\t%s, %s' % (current_violation_code,"%.2f" %round(avg_weekend, 2), "%.2f" %round(avg_weekday, 2)))
            #process the output for new k
        current_violation_code = violation_code
        current_weekend = 0
        current_weekday = 0
        if(day_type == "Weekend"):
            current_weekend = 1
        elif(day_type == "Weekday"):
            current_weekday = 1
        else:
            pass
#The last key and value
if(current_violation_code == violation_code):
    try:
        avg_weekend = current_weekend/weekends
        avg_weekday = current_weekday/weekdays
    except:
        avg_weekend = current_weekend
        avg_weekday = current_weekday
#forget to output the last word if needed!
if current_violation_code:
    print ('%s\t%s, %s' % (current_violation_code,"%.2f" %round(avg_weekend, 2), "%.2f" %round(avg_weekday, 2)))


