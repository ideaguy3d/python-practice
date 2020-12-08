import pandas as pd

df = pd.read_csv('cancer_data.csv')
first_5_rows = df.head()

for i, v in enumerate(df.columns):
    print(i, v)

debug = 1