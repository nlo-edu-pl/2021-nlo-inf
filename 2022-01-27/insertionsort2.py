def wizualizuj(tablica):
    "Tekstowa wizualizacja tablicy"
    for x in tablica:
        print(f'{x:3d} {"#" * x}')
    print()

def insertion_sort(tablica):
    "Insertion sort in-place"
    for i in range(1, len(tablica)):
        j = i
        print(f'Element #{i} {tablica[i]}')
        while j > 0 and tablica[j-1] > tablica[j]:
            print(f"przesuwam {j}")
            tablica[j-1], tablica[j] = tablica[j], tablica[j-1]
            j -= 1
        wizualizuj(tablica)


liczby = [5, 2, 10, 9, 12, 3, 1, 15, 19, 6, 4, 11]

insertion_sort(liczby)

print(f'{liczby = }')
