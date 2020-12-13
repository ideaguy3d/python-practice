import numpy as np
import pandas as panda

red_df = panda.read_csv('data/winequality-red.csv')
whi_df = panda.read_csv('data/winequality-white.csv')

red_df.rename(columns={'total_sulfur-dioxide': 'total_sulfur_dioxide'}, inplace=True)

# create color array for red dataframe
color_red = np.repeat('red', red_df.shape[0])
# create color array for white dataframe
color_white = np.repeat('white', whi_df.shape[0])

# add a new column
red_df['color'] = color_red
whi_df['color'] = color_white

# append dataframes
wine_df = whi_df.append(red_df)
print(wine_df.head(100))

wine_df.to_csv('data/wine_equality_edited.csv', index=False)



debug = 1



# end of file