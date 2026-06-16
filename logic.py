import json

import pandas as pd

from .db_connection import get_engine


def add_data(file):
    df = pd.read_csv(file.stream)
    df.to_sql(
        name='data_set',
        con=get_engine(),
        if_exists='replace',
        index=False
    )

    mean_values = df.mean(numeric_only=True).to_frame().T
    mean_values.to_sql(
        name='data_means',
        con=get_engine(),
        if_exists='replace',
        index=False
    )
    median_values = df.median(numeric_only=True).to_frame().T
    median_values.to_sql(
        name='data_medians',
        con=get_engine(),
        if_exists='replace',
        index=False
    )
    corr_matrix = df.corr(numeric_only=True)
    corr_matrix.to_sql(
        name='data_correlations',
        con=get_engine(),
        if_exists='replace',
        index=False
    )


def get_stats():
    sql_means = 'SELECT * FROM data_means'
    df_means = pd.read_sql_query(sql_means, con=get_engine())
    sql_medians = 'SELECT * FROM data_medians'
    df_medians = pd.read_sql_query(sql_medians, con=get_engine())
    sql_corr = 'SELECT * FROM data_correlations'
    df_correlations = pd.read_sql_query(sql_corr, con=get_engine())
    means = df_means.to_dict(orient='records')[0]
    medians = df_medians.to_dict(orient='records')[0]
    parameters = df_correlations.columns.to_list()
    correlation_matrix = df_correlations.to_numpy().tolist()
    correlations = df_correlations.to_dict(orient='records')
    correlations2 = {'variables': parameters, 'correlation_matrix': correlation_matrix}
    
    ans = {
        'mean_values': means,
        'median_values': medians,
        'correlations_coefficients': correlations2
    }
    return json.dumps(ans)
