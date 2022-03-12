"""
Unit Test practice
"""


def cuboid_volume(length):
    if type(length) not in [int, float]:
        raise TypeError('EXCEPTION: The length must be an int or float')
    return length ** 3


if __name__ == '__main__':
    length_input = [2, 1.1, -2.5, 2j, 'two']

    for i in length_input:
        print(cuboid_volume(i))


pass
