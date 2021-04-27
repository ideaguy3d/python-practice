import matplotlib.pyplot as plt
import statistics
import time
import copy


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


def deep_shallow_copy():
    list1 = [0, 1, 2]
    list2 = [7, 8, 9]
    compoundList1 = [list1, list2]

    # assignment operation
    compoundList2 = compoundList1
    print(id(compoundList1) == id(compoundList2))  # True
    print(id(compoundList1[0]) == id(compoundList2[0]))  # True

    # shallow copy
    compoundList2 = copy.copy(compoundList1)
    print(id(compoundList1) == id(compoundList2))  # Falsed
    print(id(compoundList1[0]) == id(compoundList2[0]))  # True

    # deep copy
    compoundList2 = copy.deepcopy(compoundList2)
    print(id(compoundList1) == id(compoundList2))  # False
    print(id(compoundList1[0]) == id(compoundList2[0]))  # False


def permute(input_list):
    final_compound_list = []
    if len(input_list) == 0:
        final_compound_list.append([])
    else:
        first_elem = input_list[0]
        rest_list = input_list[slice(1, None)]
        # RECURSIVE CALL
        sub_compound_list = permute(rest_list)
        for a_list in sub_compound_list:
            for j in range(0, len(a_list) + 1):
                b_list = copy.deepcopy(a_list)
                b_list.insert(j, first_elem)
                final_compound_list.append(b_list)
    return final_compound_list


def permute2(input_list):
    final_compound_list = []
    if len(input_list) == 0:
        final_compound_list.append([])
    else:
        first_elem = input_list[0]
        rest_list = input_list[slice(1, None)]
        subcompound_list = permute2(rest_list)
        for a_list in subcompound_list:
            for i in range(0, len(a_list) + 1):
                b_list = copy.deepcopy(a_list)
                b_list.insert(i, first_elem)
                final_compound_list.append(b_list)
    return final_compound_list


def permutations(string):
    return return_permutations(string, 0)


def return_permutations(string, index):
    output = []
    if index >= len(string):
        return [""]
    small_output = return_permutations(string, index + 1)
    cur_char = string[index]
    for sub_str in small_output:
        for i in range(len(small_output[0]) + 1):
            new_sub_str = sub_str[0:i] + cur_char + sub_str[i:]
            output.append(new_sub_str)
    return output

print("\n")
print(permutations('abc'))
"""
deep_shallow_copy()
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
