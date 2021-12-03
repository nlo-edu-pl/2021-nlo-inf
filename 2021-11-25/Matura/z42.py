import z4

ile = 0

with open("liczby.txt") as f:
    for l in f:
        l = int(l)
        if z4.czy_wesola(l):
            ile += 1

print(f"{ile=}")

