#!/usr/bin/python3

import random

with open("parametry.txt") as f:
    d = f.read().split()
    n, w, h = d
    n = int(n)
    w = float(w)
    h = float(h)

with open("punkty.txt", "w") as f:
    for i in range(n):
        x = random.uniform(0, w)
        y = random.uniform(0, h)
        f.write(f"{x:.2f},{y:.2f}\n")

