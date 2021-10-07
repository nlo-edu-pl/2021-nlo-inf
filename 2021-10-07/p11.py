"""
autor: Maks Sz.

11. Dla podanego wzrostu i waga zwraca BMI.
"""

def jakie_bmi(wzrost: float, masa: float) -> float:
    return masa / (wzrost ** 2)

assert jakie_bmi(1.8, 70) > 19
assert jakie_bmi(1.8, 70) < 30

# uwaga, to może być problematyczne:
assert jakie_bmi(1.8, 70) == 21.604938271604937

# print(jakie_bmi(1.8, 70))
