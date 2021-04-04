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


def generator_practice_3():
    correct = [[1, 2, 3],
               [2, 3, 1],
               [3, 1, 2]]

    incorrect = [[1, 2, 3, 4],
                 [2, 3, 1, 3],
                 [3, 1, 2, 3],
                 [4, 4, 4, 4]]

    incorrect2 = [[1, 2, 3, 4],
                  [2, 3, 1, 4],
                  [4, 1, 2, 3],
                  [3, 4, 1, 2]]

    incorrect3 = [[1, 2, 3, 4, 5],
                  [2, 3, 1, 5, 6],
                  [4, 5, 2, 1, 3],
                  [3, 4, 5, 2, 1],
                  [5, 6, 4, 3, 2]]

    incorrect4 = [['a', 'b', 'c'],
                  ['b', 'c', 'a'],
                  ['c', 'a', 'b']]

    incorrect5 = [[1, 1.5],
                  [1.5, 1]]

    def rules(row: list, sq_len: int) -> bool:
        dedupe = set(row)
        all_int = all(map(lambda x: isinstance(x, int), row))
        if all_int or len(dedupe) != sq_len or max(dedupe) != sq_len:
            return False
        else:
            return True

    def check_sudoku1(board: list) -> bool:
        sq_len = len(board)
        columns = [[] for _ in range(sq_len)]
        for row in board:
            if not rules(row, sq_len):
                return False
            # get all columns
            for i, column in enumerate(row):
                columns[i].append(column)
        for row in columns:
            if not rules(row, sq_len):
                return False
        return True

    def check_sudoku(square: list) -> bool:
        for row in square:
            check_list = list(range(1, len(square[0]) + 1))
            for column in row:
                if column not in check_list:
                    return False
                check_list.remove(column)
        for n in range(len(square[0])):
            check_list = list(range(1, len(square[0]) + 1))
            for row in square:
                if row[n] not in check_list:
                    return False
                check_list.remove(row[n])
        return True

    check_sudoku(incorrect4)


generator_practice_3()

# end of file
