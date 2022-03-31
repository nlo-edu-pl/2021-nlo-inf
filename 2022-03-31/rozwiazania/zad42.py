import zad4

pary = zad4.wczytaj_pary()
pary.sort()

print("Wynik:")
for a, b in pary:
    print(a, b)
print(f'{len(pary) = }')
