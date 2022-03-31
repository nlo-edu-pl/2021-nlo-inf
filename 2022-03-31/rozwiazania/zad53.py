import sqlite3

db = sqlite3.connect('zad5.db')

print("Zad 5.3")
sql = """
    Select
        (rok / 10) || 'x' As dekada,
        count() As ile
    From (
        Select
            pesel,
            1900 
                + Substr(pesel, 1, 2)
                + (Substr(pesel, 3, 1) / 2 * 100) As rok
        From punktszczepien
    ) As x
    Group By dekada;
"""

for r in db.execute(sql):
    print(r, r[1]//5 * "#")

