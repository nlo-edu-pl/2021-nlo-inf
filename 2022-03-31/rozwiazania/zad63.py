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
    From uczniowie;
""")

db.execute("""
    Create Temporary View uczniowie_oceny As
    Select
        *,
        Case
            When ile_ptk*2 >= 98 Then 6
            When ile_ptk*2 >= 90 Then 5
            When ile_ptk*2 >= 75 Then 4
            When ile_ptk*2 >= 50 Then 3
            When ile_ptk*2 >= 30 Then 2
            Else 1
        End As ocena
    From uczniowie_punkty
""")

sql = """
Select ocena, count() as ile
From uczniowie_oceny
Group By ocena
Order By ocena Desc
"""

for r in db.execute(sql):
    print(r)
