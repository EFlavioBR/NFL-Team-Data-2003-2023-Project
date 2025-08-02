import pandas as pd
import numpy as np 
df = pd.read_csv('team_stats_2003_2023.csv')

#QUESTÃO 1 Qual foi a média de pontos marcados (points) pelo 'Green Bay Packers' nas temporadas em que eles tiveram 11 ou mais vitórias (wins)?

print("Média de pontos dos packers com 11+ vitórias")
#filtrando
packers_wins = df[(df['team'] == 'Green Bay Packers') & (df['wins'] >= 11)]
avg_points = packers_wins['points'].mean()

print(f"A média de pontos dos Packers em temporadas com 11 + vitórias foi: {avg_points:.2f}\n")
print("-" * 50)

# 5 temporadas, de toda a liga, em que um time teve a defesa mais frágil, ou seja, sofreu mais pontos

print("\n--- as piores 5 defesas(mais pontos sofridos) ---")

worst_defences = df.sort_values(by='points_opp', ascending=False)
print(worst_defences[['year', 'team', 'wins', 'points_opp']].head(5))