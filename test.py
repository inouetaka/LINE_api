import pandas as pd
import json

output = {}
poke = pd.read_csv('poke.csv', index_col=0)
print(poke.loc[1])

for p in range(len(poke)):
    info = poke.loc[p]
    id = info['number']
    name = info['name']
    type_ = info['type'].split("https://")[1]
    img = info['img'].split("https://")[1]
    print(img)
