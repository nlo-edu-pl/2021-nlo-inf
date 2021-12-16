import zad4
lw =0
nazwapliku = "2021-12-16/liczby.txt"

with open(nazwapliku) as f:
    for linia in f:
        liczba = int(linia)
        # print(liczba) 
        if zad4.czy_wesola(liczba):
            lw = lw + 1
print(lw)