"""
Przykładowa implementacja mergesort()
"""

def merge(tablica_a: list, tablica_b: list) -> list:
    """Funkcja scalająca dwie uporządkowane listy"""
    print(f"merge {tablica_a} {tablica_b}")
    wynik = []

    while True:
        elem_a, elem_b = tablica_a[0], tablica_b[0]

        if elem_a < elem_b:
            wynik.append(elem_a)
            del tablica_a[0]
        else:
            wynik.append(elem_b)
            del tablica_b[0]

        if len(tablica_a) == 0:
            wynik.extend(tablica_b)
            break

        if len(tablica_b) == 0:
            wynik.extend(tablica_a)
            break

    return wynik

def mergesort(tab):
    """Implementacja rekurencyjna"""
    print(f"Mergesort {tab}")
    if len(tab) <= 1:
        return tab
    lewa = mergesort(tab[0:len(tab)//2])
    prawa = mergesort(tab[len(tab)//2:])
    return merge(lewa, prawa)

liczby = [1, 3, 5, 7, 2, 2, 3, 2, 1, 7, 8]

print(mergesort(liczby))

#assert merge([1], [2]) == [1, 2]
# assert merge([1, 2, 3], [5, 6, 7]) == [1, 2, 3, 5, 6, 7]
