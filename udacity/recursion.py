import matplotlib.pyplot as plt
import statistics
import time


def power_of_2(n):
    if n == 0:
        return 1
    return 2 * power_of_2(n - 1)


def sum_integers(n):
    if n < 1:
        return n
    return n + sum_integers(n - 1)


def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n - 1)


def reverse_string(input):
    if len(input) == 0:
        return ''
    else:
        first_char = input[0]
        the_rest = slice(1, None)
        sub_string = input[the_rest]
        reverse = reverse_string(sub_string)
        return reverse + first_char


def is_palindrome(input):
    if len(input) <= 1:
        return True
    else:
        first_char = input[0]
        last_char = input[-1]
        sub_str = input[1:-1]
        return (first_char == last_char) and is_palindrome(sub_str)


def add_one(arr):
    if arr == [9]:
        return [1, 0]
    if arr[-1] < 9:
        arr[-1] += 1
    else:
        arr = add_one(arr[:-1]) + [0]
    return arr


print("\n")

"""
print("power_of_2(5) = ", power_of_2(5))
print("--")
print("sum_integers(3) = ", sum_integers(3))
print("--")
print("Pass" if ("" == reverse_string("")) else "Fail")
print("Pass" if ("cba" == reverse_string("abc")) else "Fail")
print("Pass" if ("olleh" == reverse_string("hello")) else "Fail")
print("--")
print("Pass" if (is_palindrome("")) else "Fail")
print("Pass" if (is_palindrome("a")) else "Fail")
print("Pass" if (is_palindrome("madam")) else "Fail")
print("Pass" if (is_palindrome("abba")) else "Fail")
print("Pass" if not (is_palindrome("Udacity")) else "Fail")
"""
print("\n")

# end of file
