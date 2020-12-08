import pandas as pd

df = pd.read_csv('breast_cancer_data.csv')
df2 = pd.read_csv('student_data.csv')
df3 = pd.read_csv('student_data.csv', header=1)
df4 = pd.read_csv('student_data.csv', header=None)

labels = ['id', 'name', 'attendance', 'hw', 'test1', 'project1', 'test2', 'project2', 'final']
df5 = pd.read_csv('student_data.csv', header=0, names=labels)

# indexes
# df6 = pd.read_csv('data.csv', index_col='Name')
# df7 = pd.read_csv('data.csv', index_col=['Name', 'ID'])

first_5_rows = df.head()

for i, v in enumerate(df.columns):
    print(i, v)

df5.to_csv('student_data_header_change.csv', index=False)
print('\nWrote new data to disk.')

# dimensions,
print('\n', df.shape)
# column info,
print('\n', df.dtypes)
# traversal,
print('\n', type(df['diagnosis'][0]), df['diagnosis'][0])
# summary,
print('\n', df.info())
# unique values,
print('\n', df.nunique())
# descriptive stats,
print('\n', df.describe())
# 5 elements from the last pos on,
print('\n', df.tail(5))
# labels and indexes, Interesting syntax
df_means_label = df.loc[:, 'id':'concavity_mean']
df_means_index = df.iloc[:, :12]
df_means_index.to_csv('df_means_index.csv')
print ('\nL41 - wrote file to disk\n')

debug = 1
