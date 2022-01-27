from pytest import xfail


def wizualizuj(tablica):
    "Tekstowa wizualizacja tablicy"
    for x in tablica:
        print(f'{x:3d} {"#" * x}')
    print()


LICZNIK = 0

def insertion_sort(tablica):
    nowa = []
    for wartosc in tablica:
        wizualizuj(nowa)
        print(f'Wstawiam {wartosc} we właściwe miejsce')
        pozycja = len(nowa)
        print(f'{nowa = }')
        for p, x in enumerate(nowa):
            print(f'Porównuję {p}:  {x} z {wartosc}')
            if x > wartosc: # trzeba wstawic przed nim
                pozycja = p
                break
        nowa.insert(pozycja, wartosc)
        print(f"Trzeba wstawić na pozycji {pozycja}")
    return nowa

liczby = [5, 2, 10, 9, 12, 3, 1, 15, 19, 6, 4, 11]

liczby2 = insertion_sort(liczby)

print(f'{liczby2 = }')
print(f'{LICZNIK = }')