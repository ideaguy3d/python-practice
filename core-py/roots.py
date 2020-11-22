# this module is mainly meant to practice exceptions
# also practicing comprehensions
# also practicing generators
# also practicing other functions from the python standard library: itertools
import sys
from math import factorial
from pprint import pprint as pretty
import os
import glob
from itertools import count, islice, chain


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


def is_prime(x):
    if x < 2: return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0: return False
    return True


def dictionary_comprehension_2():
    file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
    prime = [x for x in range(101) if is_prime(x)]
    prime_square_divisors = {x * x: (1, x, x * x) for x in range(20) if is_prime(x)}
    print(prime)
    pretty(prime_square_divisors)


def itertools_practice():
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    thousand_primes_list = list(thousand_primes)[-10:]
    thousand_primes_sum = sum(islice((x for x in count() if is_prime(x)), 1000))

    print('\n- itertools output:\n')
    print(thousand_primes)
    print(thousand_primes_list)
    print(thousand_primes_sum)


def any_all_practice():
    has_any = any(is_prime(x) for x in range(1245, 1499))
    has_all = all(is_prime(x) for x in range(1245, 1499))
    all_title = all(name == name.title() for name in ['Sacramento', 'San Jose', 'Palo Alto'])


def zip_practice():
    list_1 = [3, 5, 1, 3, 56]
    list_2 = [9, 8, 2, 76, 5]
    list_3 = [5, 4, 2, 3, 9]
    # for i in zip(list_1, list_2): print(i)
    # for k, v in zip(list_1, list_2): print(f"{k} = {v}")
    temperatures = chain(list_1, list_2, list_3)
    temperatures_all = all(t > 0 for t in temperatures)
    for temps in zip(list_1, list_2, list_3):
        print(f"min = {min(temps):4.1f}, max = {max(temps):4.1f}, average = {sum(temps) / len(temps):4.1f}")


# dictionary_comprehension_2()
# itertools_practice()
zip_practice()

if __name__ == '__main__':
    run_main = False
    if run_main: main()
