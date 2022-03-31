import sqlite3

db = sqlite3.connect('zad6.db')

print("Zad 6")
sql = """
    Select 2 + 2
"""

for r in db.execute(sql):
    print(r)
