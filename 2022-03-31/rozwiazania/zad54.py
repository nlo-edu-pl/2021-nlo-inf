import sqlite3

db = sqlite3.connect('zad5.db')

print("Zad 5.4")
sql = """
    Select
        RODZAJSZCZEPIONKI,
        plec,
        count() As ile
    From (
        Select
            RODZAJSZCZEPIONKI,
            Case
                When Substr(pesel, 10, 1) % 2 == 0
                Then 'K'
                Else 'M'
            End As plec
        From punktszczepien
    ) As x
    Group By RODZAJSZCZEPIONKI, plec;
"""

for r in db.execute(sql):
    print(r)

