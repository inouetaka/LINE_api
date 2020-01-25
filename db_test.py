import sqlite3
import pandas as pd

"""
conn = sqlite3.connect("test.db")
c = conn.cursor()

c.execute('''CREATE TABLE pokes (id, name, type, image)''')

poke = pd.read_csv('poke.csv', index_col=0)
for p in range(len(poke)):
    info = poke.loc[p]
    id = info['number']
    name = info['name']
    type_ = info['type'].split("https://")[1]
    img = info['img'].split("https://")[1]

    sql = '''insert into pokes(id, name, type, image) values (?, ?, ?, ?)'''
    ins = (str(id), name, type_, img)
    c.execute(sql, ins)
    conn.commit()
conn.close()
"""

conn = sqlite3.connect("test.db")
c = conn.cursor()

c.execute('SELECT * FROM pokes WHERE name = "サルノリ"')
row = c.fetchall()
print(row[0][1])

conn.close()