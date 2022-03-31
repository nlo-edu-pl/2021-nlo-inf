import zad4

pary = zad4.wczytaj_pary()

ile = 0

for p in pary:
    a, b = p
    s = a + b
    print(a, b, s)
    if zad4.czy_trojkatna(s):
        print(p)
        ile += 1

print(f'{ile = }')
