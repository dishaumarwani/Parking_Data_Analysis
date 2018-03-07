#!/usr/bin/env python
"""
    This runs similar to word count
    but instead of printing, it stores the 
    key and value in a dictionary.
    The sorts the dictionary in descending by value
    and then then in ascending by value.
    It then prints the top 20 records.
"""
import operator
import sys

current_word = None
current_count = 0
word = None
violated_top20 = {}


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
            violated_top20[current_word] = current_count
        current_count = count
        current_word = word

# do not forget to add the last word if needed!
violated_top20[current_word] = current_count

#Sort in descending by key and ascending by value
violated_top20 = [v for v in sorted(violated_top20.items(), key=lambda kv: (-kv[1], kv[0]))]

#Print the key, value pairs from the list violated_top20
for k_v in violated_top20[:20]:
    print(str(k_v[0])+'\t'+str(k_v[1]))

