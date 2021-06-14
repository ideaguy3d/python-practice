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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


# I added a header row to the csv file
text_header_row = texts.pop(0)
call_header_row = calls.pop(0)

text_1st_rec = texts[0]
call_last_rec = calls[len(calls)-1]

print(f'First record of texts, {text_1st_rec[0]} texts {text_1st_rec[1]} at time {text_1st_rec[2]}')
print(f'Last record of calls, {call_last_rec[0]} calls {call_last_rec[1]} at time {call_last_rec[2]}, lasting {call_last_rec[3]} seconds')



# end of file