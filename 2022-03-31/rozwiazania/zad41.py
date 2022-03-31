import zad4

liczby = zad4.wczytaj()

ile_par = 0
for n in liczby:
    ws = zad4.wspak_int(n)
    if n < 10:
        continue
    if ws < 10:
        continue
    czy_ma_pare = ws in liczby
    if czy_ma_pare:
        print(n, ws, n in liczby, ws in liczby)
        ile_par += 1

wynik = ile_par // 2

print(f"{wynik = }")
