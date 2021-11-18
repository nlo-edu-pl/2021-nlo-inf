#!/usr/bin/python3

def odleglosc(p1: tuple, p2: tuple) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def dlugosc_sciezki1(sciezka: list) -> float:
    poprzedni = sciezka[0]
    suma = 0.0
    for biezacy in sciezka[1:]:
        suma += odleglosc(poprzedni, biezacy)
    return suma

def dlugosc_sciezki(sciezka: list) -> float:
    suma = 0.0
    for poprzedni, biezacy in zip(sciezka[1:], sciezka[:-1]):
        suma += odleglosc(poprzedni, biezacy)
    return suma
