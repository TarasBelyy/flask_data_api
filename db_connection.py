from sqlalchemy import create_engine

USER = 'postgres'
PASSWORD = '1234'
HOST = 'localhost'
PORT = '5432'
DB_NAME = 'data_collection'


def get_engine():
    conn_string = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
    engine = create_engine(conn_string)
    return engine
