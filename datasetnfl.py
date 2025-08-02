import pandas as pd
df = pd.read_csv('team_stats_2003_2023.csv')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
panthers_df = df[df['team'] == 'Carolina Panthers'].copy()
print(panthers_df)