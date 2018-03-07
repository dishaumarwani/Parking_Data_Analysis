#!/usr/bin/env python

"""
    This follows a word count algorithm 
    comparing the count with max count 
    instead of printing the value. After all the 
    records have been evaluated it prints the key
"""
from operator import itemgetter
import sys

current_word = None
current_max_word = None
current_count = 0
word = None
current_max = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            if(current_max < current_count):
                current_max_word = current_word
                current_max = current_count
        current_count = count
        current_word = word


# do not forget to compare the last word if needed!
if(current_max < current_count):
    current_max_word = current_word
    current_max = current_count

# Print the key with maximum value
if current_max_word:
    print('%s\t%s' % (current_max_word, current_max))
