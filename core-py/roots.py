# this module is mainly meant to practice exceptions
# also practicing comprehensions
import sys
from math import factorial
from pprint import pprint as pretty
import os
import glob


def sqrt(x):
    """
    Compute square roots
    :param x:
    :return:
    :raises: ValueError if x is negative
    """
    if x < 0: raise ValueError(f"Cannot compute {x} because it's less than 0.")
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except (ZeroDivisionError, ValueError) as e:
        print(e, file=sys.stderr)


def comprehension_1():
    words1 = "Why sometimes I have believed as many as six impossible things before breakfast"
    words = words1.split()
    comp1 = [len(word) for word in words]
    # equivalent syntax
    lengths = []
    for word in words: lengths.append(len(word))
    print(comp1)


def comprehension_2():
    list1 = [len(str(factorial(x))) for x in range(20)]
    set1 = {len(str(factorial(x))) for x in range(20)}


def dictionary_comprehension_1():
    country_to_capital = {'United Kingdom': 'London',
                          'Brazil': 'Brasilia',
                          'Morocco': 'Rabat',
                          'Sweden': 'Stockholm'}
    capital_to_country = {capitol: country for country, capitol in country_to_capital.items()}
    pretty(capital_to_country)

def dictionary_comprehension_2():
    pass

dictionary_comprehension_1()

# if __name__ == '__main__':
#     main()
