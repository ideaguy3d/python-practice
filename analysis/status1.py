import pandas
import numpy as np
import os
from pathlib import Path

path_to_csv_files = '/Users/juliushernandez/Downloads/ryan_status_files_630pm/csv'

df_status = [pandas.read_csv(i) for i in Path(path_to_csv_files).iterdir()]

for df in df_status:
    errors = df[df['status'] == 'error']
    pass

debug = 1

## end of file