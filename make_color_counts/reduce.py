#!/usr/bin/env python

"""
    Reducer
    This is same as Word cound reducer
    The only difference being 2 keys and 1 value
"""

from operator import itemgetter
import sys
import csv

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = csv.reader([line], quotechar= '"', delimiter=',', quoting = csv.QUOTE_ALL, skipinitialspace=True)
    line = list(line)[0]   
    # parse the input we got from mapper.py
    sort_ele, column_name, word, count = line
    
    if current_word == word:
        current_count += 1
    else:
        if current_word:
            # write result to STDOUT
            print('%s\t%s, %s' % (current_column_name,current_word,current_count))
        current_count = 1
        current_word = word
        current_column_name = column_name

# do not forget to output the last word if needed!
if current_word == word:
    print('%s\t%s, %s' % (current_column_name,current_word,current_count))
