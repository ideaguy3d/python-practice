
def generator_practice_1():
    def all_even():
        n = 0
        while True:
            n += 2
            yield n

    my_gen = all_even()

    for i in range(5):
        print(f'{i}: ', next(my_gen))

    more_processing = 4
    more_processing += 20
    print(f'_> more processing {str(more_processing)}')

    for i in range(100):
        print(next(my_gen))


def generator_practice_2():
    def prod(a, b):
        return a * b

    def fact():
        i = 1
        n = i
        while True:
            output = prod(n, i)
            yield output
            n = output
            i += 1

    factorial = fact()

    for f in range(5):
        print(next(factorial))



generator_practice_2()


# end of file