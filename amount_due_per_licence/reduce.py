#!/usr/bin/env python

"""s
    The algorithm simply considers each licence type
    as key and add +1 to count and the amount value 
    to current amount for the current key.
    It averages by divding amount/count and outputs it.
"""

from operator import itemgetter
import sys

current_licence_type = None
current_count = 0
current_amount = 0
current_average = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    licence_type, amount, count = line.split('\t', 2)

    # convert count and amount (currently a string) to int
    try:
        count = int(count)
        amount = float(amount)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_licence_type == licence_type:
        current_count += count
        current_amount +=amount
    else:
        if current_licence_type:
            # write result to STDOUT
            #To avoid the program from throwing
            #divide by zero exception
            try:
                current_average = current_amount/current_count
            except ValueError:
                #the current amount will be 0.00 in this case
               current_average = current_amount
            current_amount = "{0:.2f}".format(round(current_amount,2))
            current_average = "{0:.2f}".format(round(current_average,2))
            print('%s\t%s, %s' % (current_licence_type, current_amount, current_average))
        current_count = 1
        current_amount = amount
        current_licence_type = licence_type

try:
    current_average = current_amount/current_count
except:
    current_average = current_amount
# do not forget to output the last word if needed!
if current_licence_type:
    current_amount = "{0:.2f}".format(round(current_amount,2))
    current_average = "{0:.2f}".format(round(current_average,2))
    print('%s\t%s, %s' % (current_licence_type,current_amount, current_average))
