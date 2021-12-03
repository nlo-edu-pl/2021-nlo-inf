#!/usr/bin/python3

import sqlite3
import os

try:
    os.unlink("z6.db")
except FileNotFoundError:
    pass


def decimal(x):
    return x.replace(',', '.')

db = sqlite3.connect("z6.db")
db.execute("""
        Create Table zawody (
            miejsce         Integer,
            kod_zawodnika   Text,
            odl1            Decimal,
            odl2            Decimal,
            punkty          Decimal,
            skocznia        Text
        )
""")

with open("zawody.txt") as f:
    for n, l in enumerate(f):
        if n == 0:
            continue
        m, k, o1, o2, p, s = l.split('\t') 
        m = int(m)
        o1 = decimal(o1)
        o2 = decimal(o2)
        p = decimal(p)
        s = s.strip()
        print((m, k, o1, o2, p, s))
        db.execute("""
                Insert Into zawody Select ?, ?, ?, ?, ?, ?
        """, (m, k, o1, o2, p, s))

db.execute("""
        Create Table skocznie (
            kod_skoczni     Text,
            miasto          Text,
            kod_kraju       Text,
            punkty_hs       Decimal,
            punkty_k        Decimal
        );
""")

with open("skocznie.txt", encoding='iso8859-2') as f:
    for n, l in enumerate(f):
        if n == 0:
            continue
        k, m, kraj, phs, pk = l.split('\t') 
        phs = decimal(phs)
        pk = decimal(pk)

        db.execute("""
                Insert Into skocznie Select ?, ?, ?, ?, ?
        """, (k, m, kraj, phs, pk))


db.execute("""
        Create Table skoczek (
            kod_skoczka     Text,
            nazwisko_imie   Text,
            kod_kraju       Text
        );
""")

with open("skoczek.txt", encoding='iso8859-2') as f:
    for n, l in enumerate(f):
        if n == 0:
            continue
        k, n, kraj = l.strip().split('\t')

        db.execute("""
                Insert Into skoczek Select ?, ?, ?
        """, (k, n, kraj))

db.execute("""
        Create Table punkty (
            miejsce         Integer,
            punkty          Integer
        );
""")
with open("punkty.txt", encoding='iso8859-2') as f:
    for n, l in enumerate(f):
        if n == 0:
            continue
        m, p = l.split('\t')
        p = decimal(p)

        db.execute("""
                Insert Into punkty Select ?, ?
        """, (m, p))

db.execute("""
        Create Table kraje (
            kod_kraju       Text,
            nazwa           Text
        );
""")

with open("kraje.txt", encoding='iso8859-2') as f:
    for n, l in enumerate(f):
        if n == 0:
            continue
        k, n = l.split('\t')
        n = n.strip()

        db.execute("""
                Insert Into kraje Select ?, ?
        """, (k, n))

db.commit()
db.close()

