import os
import pandas
from pandas import isnull

def mem_mib(df):
	print("{0:.2f} MB".format(
		df.memory_usage().sum() / (1024 * 1024)
	))

def make_categorical(df, col_name):
	df.loc[:, col_name] = pandas.Categorical(df[col_name])

master_df = pandas.read_csv(os.path.join('..', 'data', 'master.csv'))
master_df_cp = master_df.copy()
# drop any rows where the playerID is null
master_df = master_df.dropna(subset=['playerID'])
# drop rows if BOTH firsName and lastName are null (how='all')
master_df = master_df.dropna(subset=['firstName', 'lastName'], how='all')
# only analyze data if player was born after 1900
master_df = master_df.loc[master_df['birthYear'] >= 1900]
# set a new index
master_df = master_df.set_index("playerID")

columns_to_keep = ['playerID', 'coachID', 'firstName', 'lastName', 'birthYear', 'birthMon', 'birthDay']

print(master_df[columns_to_keep].head())

# use .filter() for regex
master_df = master_df.filter(regex='(playerID|^birth)|(Name$)')

print(master_df.shape)
print(master_df.columns)

birth_year_counts = master_df['birthYear'].value_counts()

# ♥ using .Categorical()
birth_year_categories = pandas.Categorical(master_df['birthYear'])
make_categorical(master_df, 'birthYear')
make_categorical(master_df, 'birthMon')

playerId_nulls = isnull(master_df["playerID"]).value_counts()

mem_mib(master_df)
mem_mib(master_df_cp)



debug = 1