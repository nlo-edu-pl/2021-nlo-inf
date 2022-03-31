import sqlite3

db = sqlite3.connect('zad5.db')

print("Zad 5.1")
sql = """
    Select
        Max(pesel) As najmlodsza,
        Min(pesel) As najstarsza
    From punktszczepien;
"""

for r in db.execute(sql):
    print(r)
