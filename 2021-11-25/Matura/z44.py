#!/usr/bin/python3

import z4

def czy_pierwsza(n: int) -> bool:
    for dzielnik in range(2, n):
        if n % dzielnik == 0:
            return False
    return True


ile = 0
with open('liczby.txt') as f:
    for l in f:
        l = int(l)
        if czy_pierwsza(l) and z4.czy_wesola(l):
            ile += 1
            print(l)
print(f"{ile = }")
