

def merge(tablica_a: list, tablica_b: list) -> list:
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

x = merge([1, 2, 3], [2, 2.7, 7])
print(x)


#assert merge([1], [2]) == [1, 2]
# assert merge([1, 2, 3], [5, 6, 7]) == [1, 2, 3, 5, 6, 7]
