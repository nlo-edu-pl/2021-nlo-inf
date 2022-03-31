import sqlite3

db = sqlite3.connect('zad6.db')

print("Zad 6")

db.execute("""
        Create Temporary View klasa_plec As
        Select
            klasa,
            plec,
            count() As ile
        From uczniowie
        Group By klasa, plec;
""")

sql = """
    Select
        kp1.klasa,
        Round(1.0 * kp1.ile / (kp1.ile + kp2.ile), 2) As udzial_m
    From klasa_plec kp1
    Join klasa_plec kp2 On kp1.klasa == kp2.klasa And kp1.plec != kp2.plec
    Where
        kp1.plec == 'm'
        And 1.0 * kp1.ile / (kp1.ile + kp2.ile) > 0.25
"""



for r in db.execute(sql):
    print(r)
