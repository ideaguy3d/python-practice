import pandas as panda
import numpy as np

df = panda.read_csv('data/breast_cancer_data.csv')
df2 = panda.read_csv('data/student_data.csv')
df3 = panda.read_csv('data/student_data.csv', header=1)
df4 = panda.read_csv('data/student_data.csv', header=None)

labels = ['id', 'name', 'attendance', 'hw', 'test1', 'project1', 'test2', 'project2', 'final']
df5 = panda.read_csv('data/student_data.csv', header=0, names=labels)

# indexes
# df6 = panda.read_csv('data.csv', index_col='Name')
# df7 = panda.read_csv('data.csv', index_col=['Name', 'ID'])

first_5_rows = df.head()

for i, v in enumerate(df.columns): print(i, v)

df5.to_csv('data/student_data_header_change.csv', index=False)
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
df_means_index.to_csv('data/df_means_index.csv')
print ('\nL41 - wrote file to disk\n')


# use numpy to select multiple ranges
range_1 = np.r_[1:10, 15, 19]
#print('\n_> Printing range_1: \n', range_1)
#df_range_1 = df.iloc[:, range_1]


# fill empty values with the mean
df_area_mean = df['area_mean'].mean()
df['area_mean'].fillna(df_area_mean, inplace=True)
# or
df['area_mean'] = df['area_mean'].fillna(df_area_mean)

# deal w/dupes
print(df.duplicated())
print(sum(df.duplicated()))
df.drop_duplicates(inplace=True)

# data cast, check with df.info()
convert_timestamp = False
if convert_timestamp: df['timestamp'] = panda.to_datetime(df['timestamp'])

df_breast_cancer_means = panda.read_csv('data/cancer_data_means.csv')
columns = df_breast_cancer_means.columns
new_list = []
for c in columns:
    if '_mean' in c: new_list.append(c[:-5])
    else: new_list.append(c)

# change column names
df_breast_cancer_means.columns = new_list
df.to_csv('cancer_data_edited.csv', index=False)

df_breast_cancer_means.hist(figsize=(8,8))


df_power_plant = panda.read_csv('data/power_plant.csv')
df_power_plant.plot(x='')




debug = 1
