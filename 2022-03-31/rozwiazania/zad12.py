#!/usr/bin/env python3

import math

TekstJ = "Czytanie książek to najpiękniejsza zabawa, jaką sobie ludzkość wymyśliła."

N = 4

rozm = N * N
ile_bl = math.ceil(len(TekstJ)/rozm)
TekstZ = ""

for nbloku in range(ile_bl):
    blok = TekstJ[rozm*nbloku:rozm*(nbloku+1)]
    while len(blok) < rozm:
        blok += "X"
    blok_wyn = ""
    for x in range(N):
        for y in range(N):
            poz = y * N + x
            blok_wyn += blok[poz]
    TekstZ += blok_wyn

print(TekstZ)

