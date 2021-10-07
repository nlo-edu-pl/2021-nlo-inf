"""
Dla podanej pary liczb całkowitych funkcja zwraca informację, czy ich iloczyn jest podzielny przez 7.
"""

def czy_iloczyn_podzielny_przez_siedem(a: int, b: int) -> bool:
    if (a * b) % 7 == 0:
        return True
    else:
        return False


if czy_iloczyn_podzielny_przez_siedem(13, 11):
    print("Tak")
else:
    print("Nie")
