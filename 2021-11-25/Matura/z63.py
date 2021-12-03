#!/usr/bin/python3

import sqlite3

db = sqlite3.connect("z6.db")

sql = """
    Select
        kod_zawodnika,
        odl1,
        odl2,
        odl1 + odl2 As os,
        s.*,
        k.nazwa
    From zawody z
    Join skoczek s On (s.kod_skoczka == z.kod_zawodnika)
    Join kraje k On (k.kod_kraju == s.kod_kraju)
    Order By odl1+odl2
    Limit 1
"""

for x in db.execute(sql):
    print(f"{x = }")

