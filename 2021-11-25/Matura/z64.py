#!/usr/bin/python3

import sqlite3

db = sqlite3.connect("z6.db")

sql = """
    Select
        za.punkty,
        za.miejsce,
        sk.nazwisko_imie,
        p.punkty,
        za.punkty + p.punkty As razem
    From zawody za
    Join skoczek sk On sk.kod_skoczka == za.kod_zawodnika
    Join punkty p On p.miejsce == za.miejsce
    Order By razem Desc
    Limit 3
"""

for x in db.execute(sql):
    print(f"{x = }")

