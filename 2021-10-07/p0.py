"""
Dla podanej pary liczb całkowitych funkcja zwraca informację, czy ich iloczyn jest podzielny przez 7.
"""

def czy_iloczyn_podzielny_przez_siedem(a: int, b: int) -> bool:
    return (a % 7 == 0) or (b % 7 == 0)


if czy_iloczyn_podzielny_przez_siedem(13, 77):
    print("Tak")
else:
    print("Nie")
