import pandas as pd
import json

output = {}
poke = pd.read_csv('poke.csv', index_col=0)
result = poke[poke['name'] == 'サルノリ']
print(result['type'][0])
num = result['number'][0]

#print(num)

