import sqlite3

db = sqlite3.connect('zad5.db')

print("Zad 5.1")

db.execute("""
Create Temporary View t1 As
    Select 
        pesel,
        1900
           + Substr(pesel, 1, 2)
           + (Substr(pesel, 3, 1) / 2 * 100)
        As rok,
        Substr(pesel, 3, 2) % 20 As miesiac,
        Substr(pesel, 5, 2) As dzien
    From punktszczepien
""");


sql = """
    Select
        rok, miesiac, dzien, pesel
    From t1
    Order By rok, miesiac, dzien
    Limit 1;
"""

for r in db.execute(sql):
    print(r)

sql = """
    Select
        rok, miesiac, dzien, pesel
    From t1
    Order By rok DESC, miesiac DESC, dzien DESC
    Limit 1;
"""

for r in db.execute(sql):
    print(r)
