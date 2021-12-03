#!/usr/bin/python3

import sqlite3

db = sqlite3.connect("z6.db")

sql = """
    Select * From zawody Order By punkty
"""

for x in db.execute(sql):
    print(f"{x = }")

