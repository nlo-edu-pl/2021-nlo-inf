def odleglosc(p1: tuple, p2: tuple) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def dlugosc_sciezki(sciezka: list) -> float:
    calkowita = 0.0
    for i in range(1, len(sciezka)):
        biezacy = sciezka[i]
        poprzedni = sciezka[i-1]
        odl = odleglosc(biezacy, poprzedni)
        calkowita += odl
        # print(biezacy, poprzedni, odl)
    return calkowita


# p1 = (0, 0)
# p2 = (0, 5)
# assert odleglosc(p1, p2) == 5.0

# print(f"{odleglosc((0, 5), (5, 0))=}")

# punkty = [
#     (0, 0),
#     (3, 0),
#     (3, 3),
#     (7, 0)
# ]

# print("HEJ! OTO MOJ PROGRAM")

# print(dlugosc_sciezki(punkty))

# if __name__ == '__main__':
#     print("Hej")
