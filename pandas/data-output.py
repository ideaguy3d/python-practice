import pandas
import os
import sqlite3
import sqlalchemy

df = pandas.read_pickle(os.path.join('..', 'data', 'data_frame.pickle'))
small_df = df.iloc[49980:50019, :].copy()
path = '../data/'

# excel
output_excel = False
if output_excel:
    # ModuleNotFoundError: No module named 'openpyxl'
    small_df.to_excel('basic.xlsx')
    small_df.to_excel(f'{path}no_index.xlsx', index=False)
    small_df.to_excel(f'{path}columns.xlsx', columns=['artist', 'title', 'year'])
    # ModuleNotFoundError: No module named 'xlsxwriter'
    writer = pandas.ExcelWriter('multiple_sheets.xlsx', engine='xlsxwriter')
    small_df.to_excel(writer, sheet_name="Preview", index=False)
    df.to_excel(writer, sheet_name="Complete", index=False)
    writer.save()

# sql
output_sql = False
if output_sql:
    # sqlalchemy.exc.ArgumentError: Could not parse rfc1738 URL from string 'mysql:dbname=hack_match;host=localhost;user=root;password=""'
    with sqlalchemy.create_engine('mysql:dbname=hack_match;host=localhost;user=root;password=""') as conn:
        small_df.to_sql('Tate', conn)

# json
output_json = True
if output_json:
    small_df.to_json('default.json')
    small_df.to_json('table.json', orient='table')


debug = 1

# end of file
