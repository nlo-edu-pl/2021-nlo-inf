import sqlite3

db = sqlite3.connect('zad6.db')

db.execute("""
    Create Temporary View trudnosc_pytan As
    Select
        ID_pytania,
        Avg(punkty) as trudnosc
    From punkty
    Group By ID_pytania;
""")

print("Zad 6.5")

sql = """
Select * From (Select Id_pytania, trudnosc From trudnosc_pytan Order by trudnosc Limit 1)
Union All
Select * From (Select Id_pytania, trudnosc From trudnosc_pytan Order by trudnosc Desc Limit 1);
"""

for r in db.execute(sql):
    print(r)
