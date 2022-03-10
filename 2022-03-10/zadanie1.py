def counting_sort(liczby: list) -> list:
    """Sortowanie przez zliczanie liczb od 0 do 99"""
    ...

def count_values(liczby: list) -> list:
    """Policz wystąpienia liczb"""
    licznik = [0] * 100
    for x in liczby:
        licznik[x] += 1
    return licznik

liczby = [5, 7, 11, 3, 3, 5, 9, 10, 34, 56, 56, 5, 7]


print(count_values(liczby))

# assert counting_sort(liczby) == [3, 3, 5, 5, 5, 7, 7, 9, 10, 11, 34, 56, 56]
