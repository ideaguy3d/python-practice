import numpy as np
import pandas


def group_practice_one():
    df = pandas.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                           'key2': ['one', 'two', 'one', 'two', 'one'],
                           'data1': np.random.randn(5), 'data2': np.random.randn(5)})
    print(df)
    for (k1, k2), group in df.groupby(['key1', 'key2']):
        print(f"\n\nk1: {k1}, k2: {k2}")
        print(group)
    one_liner = dict(list(df.groupby('key1', axis=0)))
    # are equivalent
    g1a = df.groupby('key1')['data1']
    g1b = df['data1'].groupby(df['key1'])
    # are equivalent
    g2a = df.groupby('key1')[['data1']]
    g2b = df[['data1']].groupby(df['key1'])
    g3a = df.groupby(['key1', 'key2'])[['data2']].mean()
    grps = [
        'g1a', g1a,
        'g1b', g1b,
        'g2a', g2a,
        'g2b', g2b,
        'g3a', g3a
    ]
    print(grps)
    debug = 1


# end of file
