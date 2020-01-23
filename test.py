import pandas as pd

poke = pd.read_csv('poke.csv')
result = poke[poke['name'] == 'サルノリ,1,001'].to_json(force_ascii=False)
print(result)