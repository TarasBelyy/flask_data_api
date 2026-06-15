import io
import pandas as pd

from .db_connection import engine


def add_data(file):
    df = pd.read_csv(file.stream)
    df.to_sql(name='new_data_set', con=engine, if_exists='fail', index=False)

