#!/usr/bin/python3

import z4

max_dlugosc = 0

for i in range(1, 1001):
    if z4.czy_wesola(i):
        dl = z4.dlugosc_cyklu(i)
        if dl > max_dlugosc:
            max_dlugosc = dl

te_liczby = []

for i in range(1, 1001):
    if z4.czy_wesola(i):
        if z4.dlugosc_cyklu(i) == max_dlugosc:
            te_liczby.append(i)
print(f"{max_dlugosc=}")
print(f"{te_liczby=}")
