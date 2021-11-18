import random

# Napisać program, który:
# 1. wczyta z pliku tekstowego `parametry.txt` trzy liczby:
#   - liczbę punktów (`n: int`)
#   - szerokość (`w: int` lub `float`)
#   - wysokość (`h: int` lub `float`)
# 2. Wygeneruje losowo `n` współrzędnych z zakresu od `(0, 0)` do `(w, h)` i zapisze do pliku `punkty.txt`

f = open("2021-11-18/parametry.txt")

n, w, h = f.read().split()
n = int(n)
w = float(w)
h = float(h)

with open("2021-11-18/punkty.txt", "w") as f:
    for i in range(n):
        x = random.uniform(0, w)
        y = random.uniform(0, h)
        f.write(f"{x:.3f},{y:.3f}\n")

print(f"{n=} {h=} {w=}")
