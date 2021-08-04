import pandas
import numpy as np

df = pandas.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                       'key2': ['one', 'two', 'one', 'two', 'one'],
                       'data1': np.random.randn(5),
                       'data2': np.random.randn(5)})

df2 = pandas.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                        'key2': ['one', 'two', 'one', 'two', 'one'],
                        'data1': [1, None, 3, 4, 5],
                        'data2': [11, 222, None, 44, 55],
                        'c3': [None, None, None, None, None]})

df2_sort1 = df2[df2.sort_values(by='data2').isnull().any(axis=1)]
df2_sort1_ops1 = [
    df2_sort1.any(),
    df2_sort1.any(axis=1),
    df2_sort1.isnull().any(),
    df2_sort1.isnull().any(axis=1)
]

debug_point_01 = 1

#
