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
    return n * factorial(n-1)


def reverse_string(input):
    pass


print("\n\n")
print("power_of_2(5) = ", power_of_2(5))
print("--")
print("sum_integers(3) = ", sum_integers(3))
print("--")
print("Pass" if ("" == reverse_string("")) else "Fail")
print("Pass" if ("cba" == reverse_string("abc")) else "Fail")
print("\n\n")

# end of file
