
def na_cyfry(liczba: int) -> list:
    wynik = []    
    while liczba > 0:
        wynik.append(liczba % 10)
        liczba = liczba // 10
    return wynik

def na_cyfry2(liczba: int) -> list:
    wynik = []
    for znaczek in str(liczba):
        wynik.append(int(znaczek))
    return wynik

def suma_kwadratow_cyfr(liczba: int) -> int:
    cyfry = na_cyfry(liczba)
    suma = 0
    for x in cyfry:
        suma = suma + x**2
    return suma

def czy_wesola(liczba: int) -> bool:
    widziane = []
    while True:
        # print(a, widziane)
        if liczba == 1:
            return True
        if liczba in widziane:
            return False

        widziane.append(liczba)
        liczba = suma_kwadratow_cyfr(liczba)

def kolejne_wesole(liczba: int) -> list:
    widziane = []
    while True:
        widziane.append(liczba)
        if liczba == 1:
            break
        liczba = suma_kwadratow_cyfr(liczba)
    return widziane
