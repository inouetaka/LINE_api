import pandas as pd
import json

output = {}
poke = pd.read_csv('poke.csv', index_col=0)
result = poke[poke['name'] == 'サルノリ']
output['number'] = result['number']
output['name'] = result["name"]
output['type'] = result['type']
output['img'] = result['img']

print(result)

