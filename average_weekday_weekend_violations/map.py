#!/usr/bin/env python
"""
    The average number of violations with
    that code issued per day on weekdays and weekend days.
"""

import sys
from datetime import datetime, date
import csv

#Function to find if a day is Weekday or Weekend
def find_day(date_v):
	try: 
		month, day, year = date_v.split("/")
		date_v = date(int(year), int(month), int(day))
		x = datetime.weekday(date_v)
		if(x<5):
			return 'Weekday'
		else:
			return 'Weekend'
	except:
		try:
			year, month, day = date_v.split("-")
			date_v = date(int(year), int(month), int(day))
			x = datetime.weekday(date_v)
			if x <5:
				return 'Weekday'
			else:
				return 'Weekend'
		except:
			return 'Incorrect Date Format'

def mapper():
    
    #Input from sys input
	for line in sys.stdin:
		line = csv.reader([line], delimiter=',')
		line = list(line)[0]
	        #This filters voilation code and issue date and
	        #maps the issue date to 'Weekend' or 'Weekday'
		if (len(line) == 22):
			print('%s\t%s' % (line[2], find_day(line[1])))

if __name__ == "__main__":
	mapper()
