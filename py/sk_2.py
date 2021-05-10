import numpy as np
import pandas

"""
# Create a new dataframe that omits all the unneeded columns:
sfairbnb = df[
['host_is_superhost', 'latitude', 'longitude','review_scores_rating','cancellation_policy','city','availability_365', 'neighbourhood_cleansed', 'property_type', 'room_type', 'price']]
"""

df = pandas.read_csv('listings-2.csv')
df_sfairbnb = df[['host_is_superhost', 'cancellation_policy', 'neighbourhood_cleansed', 'property_type', 'room_type',
                  'latitude', 'longitude', 'review_scores_rating', 'city', 'availability_365', 'price']]


def add_columns_1():
    new_col = ['superhost', 'cancellationpolicy', 'neighbourhood', 'propertytype', 'roomtype']

    for v in new_col:
        df_sfairbnb[v] = 'temp'

    for i, row in df_sfairbnb.iterrows():
        # t or f
        if row['host_is_superhost'] == 't':
            df_sfairbnb.iloc[i, 11] = 1
        elif row['host_is_superhost'] == 'f':
            df_sfairbnb.iloc[i, 11] = 0

        # flexible
        if row['cancellation_policy'] == 'flexible':
            df_sfairbnb.iloc[i, 12] = 1
        elif row['cancellation_policy'] != 'flexible':
            df_sfairbnb.iloc[i, 12] = 0

        # Downtown/Civic Center
        if row['neighbourhood_cleansed'] == 'Downtown/Civic Center':
            df_sfairbnb.iloc[i, 13] = 1
        elif row['neighbourhood_cleansed'] != 'Downtown/Civic Center':
            df_sfairbnb.iloc[i, 13] = 0

        # Apartment
        if row['property_type'] == 'Apartment':
            df_sfairbnb.iloc[i, 14] = 1
        elif row['property_type'] != 'Apartment':
            df_sfairbnb.iloc[i, 14] = 0

        # Private room
        if row['room_type'] == 'Private room':
            df_sfairbnb.iloc[i, 15] = 1
        elif row['room_type'] != 'Private room':
            df_sfairbnb.iloc[i, 15] = 0


def add_columns_2():
    pass

debug = 1

df.drop(df[df['SEX'].astype(int) != 1].index, inplace=True)
df.drop(df[(df['AGE_P'].astype(int) < 18) | (df['AGE_P'].astype(int) > 65)].index, inplace=True)
df.drop(df[(df['BMI'].astype(int) < 15) | (df['BMI'].astype(int) >= 50)].index, inplace=True)
df.drop(df[(df['SLEEP'].astype(int) < 1) | (df['SLEEP'].astype(int) >= 24)].index, inplace=True)
# df.drop(df[(df['RACERPI2'].astype(int) != 1) | (df['HISPAN_I'].astype(int) != 12)].index, inplace = True)
df.drop(df[df['race_white'].astype(int) != 1].index, inplace=True)

df.loc[(df['SMKNOW'] == ' '), 'SMKNOW'] = str('0')
df.loc[(df['SMKNOW'].astype(int).isin([3, 7, 8, 9])), 'SMKNOW'] = str('0')
df.loc[(df['SMKNOW'].astype(int).isin([1, 2])), 'SMKNOW'] = str('1')

df.loc[(df['R_MARITL'].astype(int).isin([1, 2, 3])), 'R_MARITL'] = str('1')
df.loc[(df['R_MARITL'].astype(int).isin([0, 4, 5, 6, 7, 8, 9])), 'R_MARITL'] = str('0')

df.to_csv("output.csv")
