import pandas as pd
import numpy as np
import os

def basic_practice():
	np_array = np.random.rand(3)
	np_array_3x2 = np.random.rand(3,2)
	pd_series = pd.Series(np_array, index=['first', 'second', 'third'])
	pd_df = pd.DataFrame(np_array_3x2)
	# give the df a header row
	pd_df.columns = ['first', 'second']
	print(pd_series['first'])
	print(pd_series[0])
	print(pd_series.index)
	# get items from a 2D np.array
	print(np_array_3x2[0,1], np_array_3x2[1,1])
	print(pd_df.columns)
	print(pd_df['second'])
	debug = 1
	

def metadata_one():
	csv_path: str = os.path.join('..', 'data', 'artwork_data.csv')
	# just read first 5 rows
	df = pd.read_csv(csv_path, nrows=5, index_col='id')
	df2 = pd.read_csv(csv_path, nrows=5, index_col='id', usecols=['id', 'artist'])
	debug = 1

def metadata_two():
	pass


#basic_practice()
metadata_one()




# end of file