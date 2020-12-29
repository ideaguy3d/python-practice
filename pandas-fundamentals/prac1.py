import pandas as pd
import numpy as np
import os
import json


def basic_practice():
	np_array = np.random.rand(3)
	np_array_3x2 = np.random.rand(12, 4)
	pd_series = pd.Series(np_array, index=['first', 'second', 'third'])
	pd_df = pd.DataFrame(np_array_3x2)
	# give the df a header row
	pd_df.columns = ['first', 'second', 'third', 'fourth']
	
	# output results
	print(pd_series['first'])
	print(pd_series[0])
	print(pd_series.index)
	# get items from a 2D np.array
	print(np_array_3x2[0, 1], np_array_3x2[1, 1])
	print(pd_df.columns)
	print(pd_df['second'])
	# get 2 columns
	print(pd_df[['third', 'fourth']])
	
	records = [('Espresso', '5$'), ('flat white', '10$'), ('Mocha', '$10'), ('Iced Vanilla', '$12')]
	rec_df = pd.DataFrame.from_records(records, columns=['Coffee', 'Price'])
	
	# ~indexing / 'reading from dataframes'~
	# df.loc[row_idx, column_idx]
	v1 = rec_df.loc[2, 'Coffee']
	# bool expr for rows, select all columns
	v2 = rec_df.loc[rec_df['Coffee'] == 'Mocha', :]
	
	# df is the artist data,
	# select 300 rows, select 3 columns
	v3 = df.iloc[100:400, [0, 1, 4]]
	# select all rows, select 4 columns
	v4 = df.iloc[:, [0, 1, 4, 5]]
	debug = 1


# create df3.pickle
def metadata_one():
	csv_path: str = os.path.join('..', 'data', 'artwork_data.csv')
	# just read first 5 rows
	df = pd.read_csv(csv_path, nrows=5, index_col='id')
	df2 = pd.read_csv(csv_path, nrows=5, index_col='id', usecols=['id', 'artist'])
	cols_to_use = ['id', 'artist', 'title', 'medium', 'year',
	               'acquisitionYear', 'height', 'width', 'units']
	df3 = pd.read_csv(csv_path, index_col='id', usecols=cols_to_use)
	df3.to_pickle(os.path.join('..', 'data', 'df3.pickle'))


def get_record_from_file(file_path, keys):
	"""
	scan 70,000 json files and return a list of tuples
	:param file_path:
	:param keys:
	:return:
	"""
	
	with open(file_path) as artwork_file:
		content = json.load(artwork_file)
	
	record = []
	for field in keys:
		record.append(content[field])
	
	debug = 1
	return tuple(record)


def read_artworks_from_json(keys):
	"""
	- Traverse the json folders
	:param keys:
	:return:
	"""
	json_root = os.path.join('..', 'data', 'artworks')
	
	artworks = []
	for root, _, files in os.walk(json_root):
		for f in files:
			if f.endswith('.json'):
				record = get_record_from_file(os.path.join(root, f), keys)
				artworks.append(record)
			break
	return pd.DataFrame.from_records(artworks, columns=keys, index="id")


# distinct, series length example
def distinct_artist():
	artists = df['artist']
	unique_artists = pd.unique(artists)
	unique_artists_len = len(unique_artists)
	debug = 1
	return [artists, unique_artists, unique_artists_len]


# filter example's
def francis_bacon_artwork():
	# 1st filtering technique
	francis_bacon = df['artist'] == 'Bacon, Francis'
	francis_bacon_counts = francis_bacon.value_counts()
	
	# 2nd filtering technique
	artist_counts = df['artist'].value_counts()
	francis_bacon_t2 = artist_counts['Bacon, Francis']
	
	debug = 1
	return [francis_bacon, francis_bacon_counts, francis_bacon_t2]


# indexing examples
def artwork_biggest_dimensions(df):
	"""
	Practice indexing, creating new columns, and a few built-in methods
	:param df:
	:return:
	"""
	# random cell val, 1035 is the column label (not the indice pos)
	artist_r1 = df.loc[1035, 'artist']
	# cell on 1st row 1st col
	artist_00 = df.iloc[0, 0]
	# 1st row all columns
	artist_0all = df.iloc[0, :]
	# 1st 2 rows, 1st 2 columns
	artist_0202 = df.iloc[0:2, 0:2]
	
	# force NaNs, "errors='coerce'" means on error: force to NaN
	nans_mask = pd.to_numeric(df['width'], errors='coerce')
	df.loc[:, 'width'] = pd.to_numeric(df['width'], errors='coerce')
	df.loc[:, 'height'] = pd.to_numeric(df['height'], errors='coerce')
	area = df['width'] * df['height']  # Series obj
	# create a new column
	df = df.assign(area=area)
	df_width_head_sort = df['width'].sort_values().head()
	df_width_tail_sort = df['width'].sort_values().tail()
	# use the built-in .max()
	largest_area = df['area'].max()
	# the idx of the .max()
	largest_area_idx = df['area'].idxmax()
	largest_area_rows = df.loc[df['area'].idxmax(), :]
	debug = 1


def groupby_practice():
	"""
	notable methods used
	- .loc()
	- .copy()
	:return:
	"""
	df_small = df.iloc[49980:50019, :].copy()
	group = df_small.groupby('artist')
	print(type(group))
	
	group_data = {}
	for name, group_df in group:
		group_data[name] = group_df
	
	# Aggregate min()
	for name, group_df in df_small.groupby('artist'):
		min_year = group_df['acquisitionYear'].min()
		print(f"{name}: {min_year}")
	
	# Transform, fill empties with the most frequent values
	def fill_values(series):
		values_counted = series.value_counts()
		if values_counted.empty:
			return series
		# .index[] on Series obj
		most_frequent = values_counted.index[0]
		new_medium = series.fillna(most_frequent)
		return new_medium
	
	def transform_df(source_df):
		group_dfs = []
		for name, group_df in source_df.groupby('artist'):
			filled_df = group_df.copy()
			filled_df.loc[:, 'medium'] = fill_values(group_df['medium'])
			group_dfs.append(filled_df)
		# .concat() on Pandas obj
		new_df = pd.concat(group_dfs)
		return new_df
	
	filled_df = transform_df(df_small)
	
	
	do_group_ops = False # will take a while if True
	if do_group_ops:
		# use SeriesGroupBy.transform()
		grouped_medium = df.groupby('artist')['medium']
		df.loc[:, 'medium'] = grouped_medium.transform(fill_values)
		# use SeriesGroupBy.agg()
		grouped_acq_year = df.groupby('artist')['acquisitionYear']
		min_acquisition_years = grouped_acq_year.agg(np.min)
		
	debug = 1


# ------------------------------------------------------------------------------------


# 'df3.pickle' was created in meta_one()
df = pd.read_pickle(os.path.join('..', 'data', 'df3.pickle'))
groupby_practice()



# x = df.loc[1035, :]
# metadata_one() # creates df3.pickle
# artwork_biggest_dimensions(df)
# francis_bacon_artwork()
# distinct_artist()
#
# keys_to_use = ['id', 'all_artists', 'title', 'medium', 'acquisitionYear', 'height', 'width', 'units']
#
# df_json_1 = read_artworks_from_json(keys_to_use)
# sample_json = os.path.join('..', 'data', 'artworks', 'a', '000', 'a00001-1035.json')
# sample_record = get_record_from_file(sample_json, keys_to_use)

# basic_practice()


# end of file
