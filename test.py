import pandas as pd

poke = pd.read_csv('poke.csv')
print(poke[poke['name'] == 'サルノリ,1,001'])