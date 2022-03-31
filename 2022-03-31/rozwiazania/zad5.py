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

print("Zad 5.2")
sql = """
    Select
        plec,
        count() As ile
    From (
        Select
            pesel,
            Case
                When Substr(pesel, 10, 1) % 2 == 0
                Then 'K'
                Else 'M'
            End As plec
        From punktszczepien
    ) As x
    Group By plec;
"""

for r in db.execute(sql):
    print(r)

print("Zad 5.3")

