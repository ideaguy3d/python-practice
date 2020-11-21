import sys # enables usage of argv
from urllib.request import urlopen

def basic_scalar_practice():
    """
    Just some basic scalar practice
    :return:
    """
    # binary, octal, hexadecimal
    b1 = 0b10
    o1 = 0o10
    h1 = 0x10
    print(b1, o1, h1)

    # casting
    cast1 = int(3.5)
    cast2 = int("404")
    cast3 = float("1.168")
    cast4 = bool([])
    cast5 = bool([1, 5, 9])
    cast6 = bool("")
    cast7 = bool("foo")
    cast8 = str(592)
    cast9 = str(1.16e-38)

    # util function
    # help(str)
    # input()
    uf = type(cast9[2])

    # scientific notation
    s1 = 3e8  # speed of light
    s2 = 1.61e-35

    # some operators
    ops = None is False  # is

def basic_while_loop_practice():
    """
    Just some basic while loop practice
    :return:
    """
    # while and for loops
    c = 5
    while c != 0:
        print(c)
        c -= 1

    # similar to
    c = 5
    while c:
        print(c)
        c -= 1

def input_practice():
    while True:
        # get input from user from repl
        response = input()
        if int(response) % 5 == 0:
            print('special number type')
            break

def string_byte_practice():
    # strings are immutable
    str1 = "hello " 'world'

    # raw string prefix string with r'
    path = r'C:\users\ideaguy3d\code'

    # strings are called sequence types which means
    # that certain common operations, eg [] notation
    str2 = 'hello earth'
    str2b = str2[4]
    str3 = str2.capitalize()  # returns a copy
    # strings are unicode
    str4 = "Vi er s\u00e5 glad for \u00e5 h\xf8re og l\u00e6re om Python"
    print('\n' + str4)

    # bytes, which are similar to strings but are not unicode
    by1 = b'hii heyy'
    norw = 'Vi er så glad for å høre og lære om Python'
    by2 = norw.encode('utf8')
    print('\n by2 \n')
    print(by2)
    by3 = by2.decode()
    print('\n by3: \n')
    print(by3)

    return str1

def dictionary_lists_practice(str1):
    # lists are mutable, are a workhorse of python data structures
    l1 = [1, 4, 9]
    l2 = ['apple', 'grape', 'blueberry']
    l1a = l1.append(l2)
    l3 = list(str1)
    l1.append(44)
    print(l1)
    l4 = [
        'verismilitude',
        'seminole',
        'magnitude'
    ]
    print(l4)

    # dict are also known as maps or associative arrays, fundamental ds
    # they are kept in insertion order as of Python 3.7
    d1 = {'San Jose': 408, 'Sacramento': 916, 'Stockton': 209}
    print(d1)

    print ("\n")

    # for-loop, if we loop over a dictionary we get the keys
    for elem in l4:
        print(elem)
    print('\n')

    for elem in d1:
        print(elem, d1[elem])

def even_or_odd(x):
    if x % 2 == 0:
        print('even')
        return
    print('odd')
    even_or_odd(5)
    even_or_odd(2)

def get_sixty_north():
    # using the urllib.request module
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
         words = line.decode('utf8').split()
         for letter in words:
             story_words.append(letter)
    story.close()
    print(story_words)


# modules are basically files
# special functions use __special__ in the pluralsight course we call it "dunder"
# __name__ allows us to detect whether a module is run as a script or imported into another module
#   if __name__ is "__main__" it is being ran as the main program
# python module: convenient import of files
# python script: convenient execution from a cli
# python program: usually composed of many modules
#print(__name__)

# if __name__ is not '__main__' the module knows it's being imported into another module
if __name__ == '__main__':
    print("File is not being imported")
    #get_sixty_north()
    print('\nProgram output:\n')


# Value vs. Identity Equality
p = [4,7,11]
q = [4,7,11]
print(p == q)
print(p is q)


# an interesting issue, leads to spam getting added over & over again if add_spam() is called without any args
def add_spam(meal=[]):
    meal.append('spam')
    print (meal)

# a better technique
def add_spam_improved(meal=None):
    if meal is None:
        meal=[]
    meal.append('spam')
    print(meal)