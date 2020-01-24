import pandas as pd
import json

output = {}
poke_origin = pd.read_csv('poke.csv')
poke = poke_origin.drop(["Unnamed: 0"], axis=1)
result = poke[poke['name'] == 'サルノリ,1,001']
output['name'] = result["name"]
output['type'] = result['type']
output['img'] = result['img']


j = json.dumps(output, default=object)
print(j)

