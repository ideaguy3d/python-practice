import pandas as panda
from sqlalchemy import create_engine

df = panda.read_csv('data/bestofrt.csv')

# Create SQLAlchemy Engine and empty bestofrt database
engine = create_engine('sqlite:///bestofrt.db')

# Store cleaned master DataFrame ('df') in a table called master in bestofrt.db
# bestofrt.db will be visible now in the Jupyter Notebook dashboard
df.to_sql('main_table', engine, index=False)

# Read the brand new data in the database back into a new pandas DataFrame.
df_gather = panda.read_sql('SELECT * FROM main_table', engine)









# end of file