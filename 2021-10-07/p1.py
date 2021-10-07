"""
autor: Maciek M.

1. Dla podanych długości boków trójkąta funkcja podaje, czy taki trójkąt może istnieć na płaszczyźnie.
"""

def czy_trojkat(a: float, b: float, c: float) -> bool:
    return (a + b > c) and (c + b > a) and (c + a > b)
    
    
# if czy_trojkat(7, 7, 7):
#     print("Tak")
# else:
#     print("Nie")
assert czy_trojkat(5, 5, 5) == True
assert czy_trojkat(1, 3, 100) == False
assert czy_trojkat(100, 3, 1) == False
assert czy_trojkat(3, 100, 1) == False
print("Koniec")