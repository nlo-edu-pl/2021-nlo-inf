def wizualizuj(tablica):
    "Tekstowa wizualizacja tablicy"
    for x in tablica:
        print(f'{x:3d} {"#" * x}')
    print()

def selection_sort(tablica):
    "Insertion sort in=place"
    for p in range(len(tablica)):
        wizualizuj(tablica)
        print(f'Szukam elementu na pozycję {p}')
        print(f'Szukam go w tablicy od pozycje {p} do końca')
        pozycja_min = p
        for i in range(p, len(tablica)):
            if tablica[i] < tablica[pozycja_min]:
                pozycja_min = i
        print(f"Znalazłem pozycję: {pozycja_min} i jest to wartość: {tablica[pozycja_min]}")
        tablica[p], tablica[pozycja_min] = tablica[pozycja_min], tablica[p] # zamiana elementów miejscami

liczby = [5, 2, 10, 9, 12, 3, 1, 15, 19, 6, 4, 11]

selection_sort(liczby)
