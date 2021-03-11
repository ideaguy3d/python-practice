'''
This is just a simple shared plaintext pad, with no execution capabilities.

When you know what language you'd like to use for your interview,
simply choose it from the dropdown in the top bar.

You can also change the default language your pads are created with
in your account settings: https://app.coderpad.io/settings

Enjoy your interview!


--


Let a, b, and c be strings of lengths n, n, and 2n, respectively. We want to determine if c can be constructed by
interleaving the two strings a and b, without changing the order of characters in a or b.

For example, “catdog” and “cdaogt” are valid interleavings from “cat” and “dog,” but “ctadog” is not.

Write a function which decides if c is an interleaving of a and b.
'''

import re


def regex_practice():
    txt = "The rain in Spain"
    r = re.search("^The.*b\S\w+$", txt)
    rstr = r.string
    rgrp = r.group()
    rspan = r.span()

    r2 = re.split()
    r3 = re.sub()
    r4 = re.findall()
    print(r)
    pass


def is_interleaving(a, b, c):
    a_list, b_list = list(a), list(b)
    ab = [*a_list, *b_list]
    letter_values = {}
    i = 0
    for v in ab:
        letter_values[v] = i
        i += 1
    # split c into a & b
    c_a, c_b, c_list = [], [], list(c)
    for v in c_list:
        if v in a_list:
            c_a.append(v)
        elif v in b_list:
            c_b.append(v)

    print('\n--\n')
    print("letter_values = ", letter_values)
    print("c_a = ", c_a)
    print("c_b = ", c_b)
    print('\n')
    pass


def run_test_suite(a, b, cs):
    for c, ans in cs:
        res = is_interleaving(a, b, c)
        if res != ans:
            print('FAIL: ' + c + ', reported ' + str(res) + ', expected ' + str(ans))
        else:
            print('PASS: ' + c + ', reported ' + str(res))


def tc0():
    a = 'dog'
    b = 'cat'
    cs = [('dcoatg', True),
          ('dcatog', True),
          ('dgcoat', False),
          ('cdogat', True)]

    for c, ans in cs:
        res = is_interleaving(a, b, c)
        if res != ans:
            print('FAIL: ' + c + ', reported ' + str(res) + ', expected ' + str(ans))
        else:
            print('PASS: ' + c + ', reported ' + str(res))


def tc1():
    a = 'dog'
    b = 'bot'
    cs = [('dbotog', True),
          ('dotbog', False),
          ('dbootg', True),
          ('dboogt', True),
          ('dobogt', True),
          ('dogbots', False)]

    for c, ans in cs:
        res = is_interleaving(a, b, c)
        if res != ans:
            print('FAIL: ' + c + ', reported ' + str(res) + ', expected ' + str(ans))
        else:
            print('PASS: ' + c + ', reported ' + str(res))


# regex_practice()

tc0()
# tc1()


# end of script