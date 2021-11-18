#!/usr/bin/python3

from funkcje import dlugosc_sciezki

with open("punkty.txt") as f:
    sciezka = []
    for linia in f.read().split("\n"):
        try:
            x, y = linia.split(",")
            x = float(x)
            y = float(y)
            sciezka.append((x, y))
        except:
            pass


dlugosc = dlugosc_sciezki(sciezka)

print(f"{dlugosc=}")
