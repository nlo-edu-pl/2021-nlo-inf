import sqlite3

db = sqlite3.connect('zad5.db')

print("Zad 5.6")
sql = """
    Select
        godz - 7,
        count(*)
    From (
        Select
            GODZINAZASZCZEPIENIA,
            Substr(GODZINAZASZCZEPIENIA, 1, 2) as godz
        From punktszczepien
    ) As x
    Group By godz
    Order By godz Desc
    Limit 1;
"""

for r in db.execute(sql):
    print(r)
