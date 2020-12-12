import pandas as pd
import zipfile
import numpy as np

unzip = False
if unzip :
    # Extract all contents from zip file
    with zipfile.ZipFile('armenian-online-job-postings.zip', 'r') as myzip:
        myzip.extractall()

# Read CSV (comma-separated) file into DataFrame
df = pd.read_csv('online-job-postings.csv')

# clean data
df_clean = df.copy()
df_clean_rename = df_clean.rename(columns={
    'ApplicationP': 'application_procedure',
    'AboutC': 'about_company',
    'RequiredQual': 'required_qualifications',
    'JobRequirement': 'job_requirements',
    'StartDate': 'start_date'
})
# how values does `start_date` have?
start_date_values = df_clean_rename.start_date.value_counts()

asap_list = ['Immediately', 'As soon as possible', 'Upon hiring',
             'Immediate', 'Immediate employment', 'As soon as possible.', 'Immediate job opportunity',
             '"Immediate employment, after passing the interview."',
             'ASAP preferred', 'Employment contract signature date',
             'Immediate employment opportunity', 'Immidiately', 'ASA', 'Asap',
             '"The position is open immediately but has a flexible start date depending on the candidates earliest availability."',
             'Immediately upon agreement', '20 November 2014 or ASAP',
             'immediately', 'Immediatelly',
             '"Immediately upon selection or no later than November 15, 2009."',
             'Immediate job opening', 'Immediate hiring', 'Upon selection',
             'As soon as practical', 'Immadiate', 'As soon as posible',
             'Immediately with 2 months probation period',
             '12 November 2012 or ASAP', 'Immediate employment after passing the interview',
             'Immediately/ upon agreement', '01 September 2014 or ASAP',
             'Immediately or as per agreement', 'as soon as possible',
             'As soon as Possible', 'in the nearest future', 'immediate',
             '01 April 2014 or ASAP', 'Immidiatly', 'Urgent',
             'Immediate or earliest possible', 'Immediate hire',
             'Earliest  possible', 'ASAP with 3 months probation period.',
             'Immediate employment opportunity.', 'Immediate employment.',
             'Immidietly', 'Imminent', 'September 2014 or ASAP', 'Imediately']

for phrase in asap_list:
    df_clean_rename.start_date.replace(phrase, 'ASAP', inplace=True)

start_date_values_recheck = df_clean_rename.start_date.value_counts()

for phrase in asap_list:
    assert phrase not in df_clean_rename.start_date.values

# Analysis & Visualization
# numerator
asap_count = df_clean_rename.start_date.value_counts()['ASAP']
# denominator, amount of non-empty start dates
non_empty_counts = df_clean_rename.start_date.count()
# percent of jobs with an urgent start date
urgent_jobs = asap_count / non_empty_counts # 0.70863049

viz = False
labels = np.full(len(df_clean.start_date.value_counts()), '', dtype=object)
labels[0] = 'ASAP'
if viz: df_clean_rename.start_date.value_counts().plot(kind='pie')








#
