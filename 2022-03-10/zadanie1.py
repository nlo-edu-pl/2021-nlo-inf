def counting_sort(liczby: list) -> list:
    """Sortowanie przez zliczanie liczb od 0 do 99"""
    wynik = []
    for wartosc, ile_powt in enumerate(count_values(liczby)):
        wynik.extend([wartosc] * ile_powt)
    return wynik

def count_values(liczby: list) -> list:
    """Policz wystąpienia liczb"""
    licznik = [0] * 100
    for x in liczby:
        licznik[x] += 1
    return licznik


def counting_sort2(liczby: list) -> list:
    """Sortowanie przez zliczanie liczb od 0 do 99"""
    licznik = [0] * 100
    for x in liczby:
        licznik[x] += 1
    wynik = []
    for wartosc, ile_powt in enumerate(licznik):
        wynik.extend([wartosc] * ile_powt)
    return wynik

liczby = [5, 7, 11, 3, 3, 5, 9, 10, 34, 56, 56, 5, 7]


print(count_values(liczby))

print(counting_sort(liczby))

assert counting_sort(liczby) == [3, 3, 5, 5, 5, 7, 7, 9, 10, 11, 34, 56, 56]
