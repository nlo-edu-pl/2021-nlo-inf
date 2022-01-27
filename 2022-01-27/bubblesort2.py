def wizualizuj(tablica):
    "Tekstowa wizualizacja tablicy"
    for x in tablica:
        print(f'{x:3d} {"#" * x}')
    print()


LICZNIK = 0

def bubble_sort(tablica):
    "Sortowanie Bubble sort in-place"

    global LICZNIK
    dlugosc = len(tablica)

    for j in range(dlugosc - 1):
        wizualizuj(tablica)
        for i in range(dlugosc - 1 - j):
            a, b = tablica[i:i+2]
            print(f'Porównuję {a} z {b}: ', end='')
            LICZNIK += 1
            if b < a:  # trzeba zamienić
                tablica[i:i+2] = b, a
                print("zamiana")
            else:
                print("OK")


liczby = [5, 2, 10, 9, 12, 3, 1, 15, 19, 6, 4, 11]

bubble_sort(liczby)
print(f'{LICZNIK = }')