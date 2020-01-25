import pandas as pd
import json

output = {}
poke = pd.read_csv('poke.csv', index_col=0)
result = poke[poke.name == "ゴリランダー"]
print("テスト", result)
num = result['number']

print(num)

