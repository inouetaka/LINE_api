import pandas as pd
import json

output = {}
poke = pd.read_csv('poke.csv', index_col=0)
print(poke)
result = poke[poke['name'] == 'サルノリ,1,001']
output['name'] = result["name"]
output['type'] = result['type']
output['img'] = result['img']

