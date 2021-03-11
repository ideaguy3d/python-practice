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
    r = re.search("^The.*\bS\w+$", txt)
    rstr = r.string
    rgrp = r.group()
    rspan = r.span()

    r2 = re.split()
    r3 = re.sub()
    r4 = re.findall()
    print(r)
    pass


def interleave_sorted(letter_map, c_letter, c_letter_len):
    for k, v in letter_map.items():
        for i, x in enumerate(c_letter):
            next_idx = i + 1
            next_elem = c_letter[next_idx] if next_idx != c_letter_len else False
            if next_elem and letter_map[x] > letter_map[next_elem]:
                return False
        return True


def is_interleaving(a, b, c):
    # create a list & map of letters
    a_list, b_list = list(a), list(b)
    a_map = {v: i for i, v in enumerate(a_list)}
    b_map = {v: i for i, v in enumerate(b_list)}

    # split c into a & b
    c_a, c_b, c_list = [], [], list(c)
    for v in c_list:
        if v in a_list:
            c_a.append(v)
        elif v in b_list:
            c_b.append(v)
        else:
            pass  # TODO: raise an exception

    # check a & c are sorted
    c_a_len, c_b_len = len(c_a), len(c_b)
    if interleave_sorted(a_map, c_a, c_a_len) and interleave_sorted(b_map, c_b, c_b_len):
        return True
    else:
        '''  
        print('\n--\n')
        print("~ INTERLEAVE NOT SORTED ~")
        print("a_map = ", a_map)
        print("b_map = ", b_map)
        print("c_a = ", c_a)
        print("c_b = ", c_b)
        print('\n')
        '''
        return False


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