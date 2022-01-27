def merge(tablica_a, tablica_b):
    print(f'Scalam {tablica_a} z {tablica_b}')
    wynik = []
    while len(tablica_a) > 0 and len(tablica_b) > 0:
        #print(f'{tablica_a = } {tablica_b = } {wynik = }')
        if tablica_a[0] > tablica_b[0]:
            elem = tablica_b.pop(0)
        else:
            elem = tablica_a.pop(0)
        wynik.append(elem)
    wynik.extend(tablica_a + tablica_b)
    return wynik

def merge_sort(tablica):
    print(f"sortuję listę: [{tablica}]")
    dlugosc = len(tablica)
    # warunek wyjścia z rekurencji
    # lista z 1 lub 0 elementów jest na pewno posortowana
    if dlugosc <= 1:
        return tablica
    a, b = tablica[0:dlugosc//2], tablica[dlugosc//2:]
    return merge(merge_sort(a), merge_sort(b))

xxx = [1, 6, 9, 10, 2, 3, 7, 9, 90]

print(merge_sort(xxx))

import random

dane = [random.randint(1,100000) for i in range(100)]

posortowane = merge_sort(dane)

assert sorted(dane) == posortowane