import pandas as pd


path_do_txt = 'data/measurements.txt'

df = pd.read_csv(
                path_do_txt,
                sep=';',
                header=None,
                names=['station', 'measure']
                 
                 )

df_agg = df.groupby('station')

df_kpi = df_agg['measure'].agg({
        'min': 'min',
        'max': 'max',
        'mean': 'mean'
        })

df_sorted = df_kpi.sort_values('station')