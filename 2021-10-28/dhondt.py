def ilorazy(liczba_mandatow: int, liczba_glosow: int) -> list:
    wynik = []
    for i in range(1, liczba_mandatow + 1):
        wynik.append(liczba_glosow // i)
    return wynik

def ilorazy_komitetu(komitet: str, ilorazy: list) -> list:
    wynik = []
    for iloraz in ilorazy:
        krotka = (iloraz, komitet)
        wynik.append(krotka)
    return wynik

def zlicz_ilorazy(ilorazy: list) -> dict:
    wynik = {}
    for iloraz, komitet in ilorazy:
        if komitet in wynik:
            wynik[komitet] = wynik[komitet] + 1
        else:
            wynik[komitet] = 1
    return wynik

# import os
# os.chdir(os.path.dirname(__file__))

mandaty = 5

wszystkie = []

with open("2021-10-28/wybory1.txt") as f:
    for linia in f:
        komitet, glosy = linia.split(":")
        glosy = int(glosy)
        print(komitet)
        i = ilorazy(mandaty, glosy)
        wszystkie = wszystkie + ilorazy_komitetu(komitet, i)
        #print(ilorazy_komitetu(komitet, i))

wszystkie.sort(reverse=True)
biorace = wszystkie[:mandaty]
ile_mandatow = zlicz_ilorazy(biorace)

print(ile_mandatow)

