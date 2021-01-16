import pandas
import numpy as np
import pprint

pretty = pprint.PrettyPrinter(indent=4)

obj2 = pandas.Series([4, 7, -5, 2], index=['a', 'b', 'c', 'd'])

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj3 = pandas.Series(sdata)
obj4 = pandas.Series(sdata, index=states)  # Utah is left out

print(obj2[['a', 'c']])
print(obj2[obj2 > 2])
print(pandas.isnull(obj4))
print(pandas.notnull(obj4))

print('\n\n')

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
new_column_order = ['year', 'state', 'pop']
frame = pandas.DataFrame(data)
frame2 = pandas.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                          index=['one', 'two', 'three', 'four', 'five', 'six'])
print(frame)
# simple to swap columns
frame = pandas.DataFrame(data, columns=new_column_order)
print(frame)
states = frame['state']
print('\nstates: \n', states)
print('\n', frame2)

frame2['debt'] = 19
print('\n', frame2)

debug = 1

# end of file
