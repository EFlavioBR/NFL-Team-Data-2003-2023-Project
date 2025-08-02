import pandas as pd
df = pd.read_csv('team_stats_2003_2023.csv')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
panthers_df = df[df['team'] == 'Carolina Panthers'].copy()
print(panthers_df)

#ordenando o df pela a coluna de vitórias em ordem decrescente
top_seasons = panthers_df.sort_values(by='wins', ascending=False)

top_5_seasons = top_seasons.head(5)

print("\nPanthers")
print(top_5_seasons[['year', 'wins']])
print(top_5_seasons.mean())

