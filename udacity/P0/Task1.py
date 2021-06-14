"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# I added a header row to the csv file
text_header_row = texts.pop(0)
call_header_row = calls.pop(0)

text_set = set()
call_set = set()

for call in calls:
    # add the calling & receiving numbers
    call_set.add(call[0])
    call_set.add(call[1])

for text in texts:
    # add the calling & receiving numbers
    text_set.add(text[0])
    text_set.add(text[1])

total_numbers = len(text_set) + len(call_set)

print(f'There are {total_numbers} different telephone numbers in the records.')

