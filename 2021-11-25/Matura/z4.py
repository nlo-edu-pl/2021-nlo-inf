#!/usr/bin/python3

def suma_kwadratow2(n: int) -> int:
    s: int = 0
    for d in str(n):
        s += int(d)**2
    return s

def suma_kwadratow(n: int) -> int:
    s: int = 0
    while n > 0:
        s += (n % 10)**2
        n = n // 10
    return s

def cyfry(n: int):
    while n > 0:
        yield n % 10
        n //= 10

def kwadraty_liczb(liczby: list):
    for liczba in liczby:
        yield liczba ** 2

def suma_kwadratow3(n: int) -> int:
    return sum(kwadraty_liczb(cyfry(n)))

def czy_wesola(n: int) -> bool:
    return cykl_wesolych(n) != False

def cykl_wesolych(n: int) -> list:
    widziane: list = [n]
    while True:
        n = suma_kwadratow(n)
        if n in widziane:
            return False
        widziane.append(n)
        if n == 1:
            return widziane

def dlugosc_cyklu(n: int) -> int:
    x: list = cykl_wesolych(n)
    assert x != False
    return len(x)
