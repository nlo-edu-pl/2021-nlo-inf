def merge(tablica_a, tablica_b):
    print(f'Scalam {len(tablica_a) = } z {len(tablica_b) = }')
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
    """Wersja nierekurencyjna
    
    https://pl.wikipedia.org/wiki/Sortowanie_przez_scalanie#Wersja_nierekurencyjna
    """
    kolejka = []
    for element in tablica:
        kolejka.append([element])
    while len(kolejka) > 1:
        a = kolejka.pop(0)
        b = kolejka.pop(0)
        kolejka.append(merge(a, b))
    return kolejka[0]

xxx = [1, 6, 9, 10, 2, 3, 7, 9, 90]

print(merge_sort(xxx))

import random

dane = [random.randint(1,100000) for i in range(1000)]

posortowane = merge_sort(dane)

assert sorted(dane) == posortowane