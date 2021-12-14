imiona = ['Maks', 'Tomek', 'Kuba', 'Zenon', 'Artur', 'Tymoteusz', 'Mateusz', 'Agnieszka']

max_dlugosc = 0
max_imie = None

for imie in imiona:
    dlugosc = len(imie)
    print(f"Sprawdzam {imie} ({dlugosc})")
    if dlugosc > max_dlugosc:
        max_dlugosc = dlugosc
        max_imie = imie

print(f"KONIEC: {max_dlugosc} = {max_imie}")

max_imie2 = max(imiona, key=len)

print(f"KONIEC: {len(max_imie2)} = {max_imie2}")