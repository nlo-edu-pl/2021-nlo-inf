import sqlite3

db = sqlite3.connect('zad6.db')

db.execute("""
    Create Temporary View trudnosc_pytan As
    Select
        punkty.ID_pytania,
        100.0 * Avg(punkty)/MAX_punktów as trudnosc
    From punkty
    Join max_pkt On punkty.id_pytania = max_pkt.id_pytania
    Group By punkty.ID_pytania;
""")

print("Zad 6.5")

sql = """
Select * From (
    Select Id_pytania, Round(trudnosc, 2)
    From trudnosc_pytan
    Order by trudnosc
    Limit 1
)
Union All
Select * From (
    Select Id_pytania, Round(trudnosc, 2)
    From trudnosc_pytan
    Order by trudnosc
    Desc Limit 1
);
"""

for r in db.execute(sql):
    print(r)
