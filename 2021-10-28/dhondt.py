# import os
# os.chdir(os.path.dirname(__file__))

mandaty = 7

with open("2021-10-21/wybory1.txt") as f:
    for linia in f:
        komitet, glosy = linia.split(":")
        glosy = int(glosy)
        print(komitet)
        print(glosy)


# partia ABC = 199999
# partia ... = ....

def ilorazy(liczba_mandatow: int, liczba_glosow: int) -> list:
    wynik = []
    for i in range(1, liczba_mandatow + 1):
        wynik.append(liczba_glosow // i)
    return wynik

assert ilorazy(0, 500) == []
assert ilorazy(1, 700) == [700]
assert ilorazy(3, 3000) == [3000, 1500, 1000]

print(ilorazy(4, 1000))
assert ilorazy(4, 1000) == [1000, 500, 333, 250]

print("ok")
