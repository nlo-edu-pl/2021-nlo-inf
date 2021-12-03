#!/usr/bin/python3

import sqlite3

db = sqlite3.connect("z6.db")

sql = """ 
    Select k.nazwa, Count() As c
    From skoczek s
    Join kraje k On (k.kod_kraju = s.kod_kraju)
    Group By k.kod_kraju
    Order By c
"""

for x in db.execute(sql):
    print(f"{x = }")

