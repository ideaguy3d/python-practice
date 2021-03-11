import math


def j_merge_sort(xset):
    set_count = len(xset)
    if 1 == set_count:
        return xset
    mid_point = math.floor(set_count / 2)
    left = xset[:mid_point]
    right = xset[mid_point:]
    return j_merge(j_merge_sort(left), j_merge_sort(right))


def j_merge(left, right):
    sorted_set = []
    l_index = 0
    r_index = 0
    l_count = len(left)
    r_count = len(right)
    while l_index < l_count and r_index < r_count:
        if left[l_index] < right[r_index]:
            sorted_set.append(left[l_index])
            l_index += 1
        else:
            sorted_set.append(right[r_index])
            r_index += 1
    while l_index < l_count:
        sorted_set.append(left[l_index])
        l_index += 1
    while r_index < r_count:
        sorted_set.append(right[r_index])
        r_index += 1
    return sorted_set


set1 = [99, 19, 55, 0, 5, 8, 9, 5, 1, 2, 0, 5, 4, 4, 3, 99, 55]
print(j_merge_sort(set1))


# end of file