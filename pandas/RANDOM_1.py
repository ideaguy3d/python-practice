import pandas
import numpy as np


def do_op(x):
    replace_op = False
    if '¡' in x:
        replace_op = True
    if replace_op:
        x = str(x).replace('¡', '°')
    return x

df = pandas.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                       'key2': ['one', 'two', 'one¡', 'two', 'one'],
                       'data1': np.random.randn(5),
                       'data2': np.random.randn(5)})

# simple df to practice grouping & other basic stuff
df2 = pandas.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                        'key2': ['one', 'two', 'one¡', 'two', 'one'],
                        'data1': [1, None, 3, 4, 5],
                        'data2': [11, 222, None, 44, 55],
                        'c3': [None, None, None, None, None]})

df2_sort1 = df2[df2.sort_values(by='data2').isnull().any(axis=1)]
df2_sort1_ops1 = [
    df2_sort1.any(),
    df2_sort1.any(axis=1),
    df2_sort1.isnull(),
    df2_sort1.isnull().any(),
    df2_sort1.isnull().any(axis=1)
]

df2['key2'] = df2['key2'].apply(do_op)

debug_point_01 = 1

#
