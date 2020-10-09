n = '\n--\n'
print(n + '~ String Practice ~')

# add an 'r' to make the string raw
raw = r'C:\foo\bar'
print(n + raw)

# triple single or double quotes can be used for multiline strings
php = '''
    go PHP 7 !
    and PHP 8!!
'''
py1 = """
    Python is 
    cool too! (: 
"""

# strings can auto concat
ac = 'pretty' ' neat' ' !!'
print(n + ac)

# parentheses concat
pc = ('PHP can be used for Artificial Intelligence'
      ', but Python is much more popular at the moment')

# strings can get used w/ index syntax & slice syntax
py = 'Python 3.8'
print(n + 'index syntax: ' + py[0] + py[-3] + py[2:4] + py[:2] + py[4:])

# python strings are immutable
# cannot do "py[0] = 'J'", must assign to a new string instead
jy = 'J' + py[1:]
print(n + jy)

# len() is a built-in for all sequence types
super34 = 'supercalifragilisticexpialidocious'
print(n + str(len(super34)))


