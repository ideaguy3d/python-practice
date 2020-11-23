import sys
from itertools import count, islice

# write text to file
f = open('people.csv', mode='wt', encoding='utf-8')
f.write('bill, gates, bill@mail.com, inactive, 4\n')
f.close()

# read text from file
g = open('people.csv', mode='rt', encoding='utf-8')
g.read(32)
g.read()
g.read()
g.seek(0)  # can only seek to 0 and g.tell()
g.readline()
g.readlines()
g.close()

# append text to a file
h = open('people.csv', mode='at', encoding='utf-8')
h.writelines(['Son of man, \n', 'You cannot say or guess,', 'for you know only, \n', ' a heap of broken images'])
h.close()


def sys_practice():
    """
    From the command the line we would type:
    $ py files.py somefile.txt
    :return:
    """
    # this line will accept an arg from the cli
    f = open(sys.argv[1], mode='rt', encoding='utf-8')
    for line in f:
        sys.stdout.write(line)
    f.close()


def sequence():
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen: c = a + n
        a = c

def write_sequence1(filename, num):
    """
    Would get used from the cli like:
    $ python recaman.py recaman.dat
    :param filename:
    :param num:
    :return:
    """
    f = open(filename, mode='rt', encoding='utf8')
    f.writelines(  (f"{r}\n" for r in islice(sequence(), num+1))  )
    f.close()

def write_sequence(filename, num):
    with open(filename, mode='rt', encoding='utf-8') as f:
        f.writelines([f"{r}\n" for r in islice(sequence(), num+1)])



# from the cli the command passed would look something like:
# $ py file-io.py somefile.csv 1000
if __name__ == '__main__':
    write_sequence(filename=sys.argv[1], num=int(sys.argv[2]))