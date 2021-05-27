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


# TODO: spend more time understanding this
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


def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):
    if num <= 1:
        return [""]
    elif 1 < num <= 9:
        return list(get_characters(num))
    last_digit = num % 10
    # recurrence
    small_output = keypad(num // 10)
    keypad_str = get_characters(last_digit)
    output = []
    for char in keypad_str:
        for item in small_output:
            output.append(item + char)
    return output


def deep_reverse(arr):
    if len(arr) < 1:
        return arr
    reversed_list = []
    for item in arr[::-1]:
        if type(item) is list:
            # recurrence
            item = deep_reverse(item)
        reversed_list.append(item)
    return reversed_list


def add(num_one, num_two):
    output = num_one + num_two
    custom_print(output, num_one, num_two)
    return output


def custom_print(output, num_one, num_two):
    print("The sum of {} and {} is: {}".format(num_one, num_two, output))


def j_print_intergers(n):
    if n < 0:
        return
    print(n)
    j_print_intergers(n - 1)


def binary_search(arr, target):
    return binary_search_func(arr, 0, len(arr) - 1, target)


def binary_search_func(arr, start_index, end_index, target):
    if start_index > end_index:
        return -1
    mid_idx = (start_index + end_index) // 2
    if target == arr[mid_idx]:
        return mid_idx
    elif target < arr[mid_idx]:
        return binary_search_func(arr, start_index, mid_idx, target)
    else:
        return binary_search_func(arr, mid_idx + 1, end_index, target)


def tower_of_hanoi(num_disks):
    tower_of_hanoi_x(num_disks, 'S', 'A', 'D')


def tower_of_hanoi_x(num_disks, source, aux, dest):
    if num_disks == 0:
        return
    if num_disks == 1:
        print(f'{source} {dest}')
        return
    tower_of_hanoi_x(num_disks - 1, source, dest, aux)
    print(f'{source} {dest}')
    tower_of_hanoi_x(num_disks - 1, aux, dest, source)


def get_alpha(num):
    return chr(num + 96)


# a few test cases: [123, 1145]
def all_codes(num):
    if num == 0:
        return [""]
    remainder = num % 100
    output_100 = []
    if remainder <= 26 and num > 9:
        # __RECURSIVE_CALL__
        output_100 = all_codes(num // 100)
        alpha = get_alpha(remainder)
        for i, elem in enumerate(output_100):
            output_100[i] = elem + alpha

    remainder = num % 10
    # __RECURSIVE_CALL__
    output_10 = all_codes(num // 10)
    alpha = get_alpha(remainder)
    for i, elem in enumerate(output_10):
        output_10[i] = elem + alpha

    output = []
    output.extend(output_100)
    output.extend(output_10)
    return output


def subsets(arr):
    return r_subsets(arr, 0)


# test case = [9, 12, 15]
def r_subsets(arr, idx):
    if idx >= len(arr):
        return [[]]
    sm_output = r_subsets(arr, idx + 1)
    output = [x for x in sm_output]
    for e in sm_output:
        cur = [arr[idx]]
        cur.extend(e)
        output.append(cur)
    return output


def staircase(n):
    if n <= 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)



print("\n")

"""
subsets([9, 12, 15])
tower_of_honoi(4)
j_print_intergers(5)
print(permutations('abc'))
keypad(354)
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
