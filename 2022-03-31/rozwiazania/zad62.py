import sqlite3

db = sqlite3.connect('zad6.db')

print("Zad 6.2")

db.execute("""
    Create Temporary View uczniowie_punkty As
    Select
        *,
        (Select
            Sum(Punkty)
            From punkty
            Where punkty.id_ucznia == uczniowie.id_ucznia
        ) As ile_ptk
    From uczniowie
    Order by nazwisko;
""")

sql = """
Select imie, nazwisko, klasa, ile_ptk From uczniowie_punkty
Where
    ile_ptk == (Select Max(ile_ptk) from uczniowie_punkty)
    Or ile_ptk == (Select Min(ile_ptk) from uczniowie_punkty);
"""

for r in db.execute(sql):
    print(r)
