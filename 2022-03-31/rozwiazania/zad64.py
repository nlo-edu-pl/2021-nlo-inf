import sqlite3

db = sqlite3.connect('zad6.db')

print("Zad 6")
sql = """
    Select
        id_pytania, punkty, count() As ile_osob
    From punkty
    Group By id_pytania, punkty
    Order By id_pytania, punkty
"""

pyt_id_prev = None
for pyt_id, punkty, ile in db.execute(sql):
    if pyt_id != pyt_id_prev:
        print(f"Pytanie {pyt_id}:")
        pyt_id_prev = pyt_id
    print(f"{punkty}ptk => {ile} osób")
