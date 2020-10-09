n = '\n--\n'
print(n + '~ List Practice ~')

# INTERESTING & NOTE WORTHY

squares = [1, 4, 9, 15, 25, 36, 49]

# slice
s1 = squares[-3:]

# must explicitly create a copy
s1_c = s1[:]

# concat
l1 = [1, 2, 3]
l2 = [3, 4, 5]
l3 = l1 + l2

print('--', l3)
print('--', s1)


def approx_size(size, kilobyte=True):
    if size < 0:
        raise ValueError('number cannot be negative')

    multiple = 1024 if kilobyte else 100

    suffixes = []

    for suffix in suffixes[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)


# some list/sequence-type methods
# .append()
squares.append(8 ** 8)

# !! IMPORTANT !! slice assignment
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
l[0:3] = ['A', 'B', 'C']  # n+1 to replace index 2
l[2:5] = []  # remove this portion of the list
print(n + 'slice assignment: ' + str(l))
l[:] = []  # clear the list

# Fibonacci
a, b = 0, 1
while a < 10:
    print(a, end=',')
    a, b = b, b + a

#
#
# end of file
print(n * 3)
