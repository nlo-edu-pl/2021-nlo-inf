def wczytaj():
    liczby = []
    with open("liczby.txt") as f:
        for l in f:
            liczby.append(int(l))
    return liczby

def wspak(n):
    return wspak_int(n)

def wspak_str(n):
    return int(str(n)[::-1])

def wspak_int(n):
    wynik = 0
    while n > 0:
        wynik *= 10
        wynik += n % 10
        n //= 10
    return wynik

def czy_pierwsza(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for dz in range(2, n):
        if n % dz == 0:
            return False
        if dz * dz > n:
            return True

def wczytaj_pary():
    liczby = wczytaj()
    pary = []
    for l in liczby:
        if l < 10:
            continue
        ws = wspak(l)
        if ws < 10:
            continue
        if czy_pierwsza(l) and czy_pierwsza(ws):
            para = [l, ws]
            para.sort()
            pary.append(para)
    return pary

def trojkatne():
    i, j = 0, 0
    while True:
        yield i
        j += 1
        i += j

def czy_trojkatna(n: int) -> bool:
    for t in trojkatne():
        if n == t:
            return True
        if t > n:
            return False

