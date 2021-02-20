import pandas
import csv
from pathlib import Path


def use_pandas():
    path_to_csv_files = '/Users/juliushernandez/Downloads/ryan_status_files_630pm/csv'
    df_status = [pandas.read_csv(i) for i in Path(path_to_csv_files).iterdir()]
    for df in df_status:
        errors = df[df['status'] == 'error']
        pass
    debug = 1


def csv_1():
    """ quick & simple way to create a table """
    csv_path = '../data/j/status.csv'
    table = []
    try:
        with open(csv_path, 'r') as status_file:
            reader = csv.reader(status_file)
            for row in reader:
                table.append(row)
            status_file.close()
            debug = 1
    except FileNotFoundError:
        print(f'{csv_path} not found')


csv_1()

# end of file