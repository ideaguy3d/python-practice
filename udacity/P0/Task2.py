"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during September 2016.".
"""

# I added a header row to the csv file
text_header_row = texts.pop(0)
call_header_row = calls.pop(0)

map_caller = {}
for call in calls:
    caller_1, caller_2 = call[0], call[1]
    duration = int(call[3])
    if caller_1 not in map_caller:
        map_caller[caller_1] = 0
    if caller_2 not in map_caller:
        map_caller[caller_2] = 0
    map_caller[caller_1] += duration
    map_caller[caller_2] += duration


num, most_time = '', 0
for caller in map_caller:
    if map_caller[caller] > most_time:
        most_time = int(map_caller[caller])
        num = caller

print(f'{num} spent the longest time, {most_time} seconds, on the phone during September 2016.')

debug = 1

# end of file
