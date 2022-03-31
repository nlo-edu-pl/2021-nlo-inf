import sqlite3

db = sqlite3.connect('zad5.db')

print("Zad 5.5")
sql = """
    Select
        Count(*) As ile
    From punktszczepien
    Where 
        (KTÓRADAWKA == 1 And RODZAJSZCZEPIONKI == 'Johnson&Johnson')
        Or (KTÓRADAWKA == 2 And RODZAJSZCZEPIONKI != 'Johnson&Johnson')
        ;
"""

for r in db.execute(sql):
    print(r)
