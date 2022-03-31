import zad4

liczby = zad4.wczytaj()

pary = []

for l in liczby:
    if l < 10:
        continue
    if not zad4.czy_pierwsza(l):
        continue
    ws = zad4.wspak(l)
    if ws < 10:
        continue
    if not zad4.czy_pierwsza(ws):
        continue
    para = l, ws
    para2 = ws, l
    if para not in pary and para2 not in pary:
        pary.append(para)

print(f'{len(pary) = }')
