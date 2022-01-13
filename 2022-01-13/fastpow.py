"""
w:= 1
dla a = m do 1   // m - ilość miejsc binarnych liczby n
    c = a-ta cyfra binarna liczby n
    jeżeli c = 0
       w:= w · w
    jeżeli c = 1
       w:= w · w · x
"""
def potega(x: int, n: int) -> int:
    bity = []
    while n > 0:
        bity.append(n % 2)
        n = n // 2
    bity.reverse()

    w = 1
    for bit in bity:
        if bit == 0:
            w = w * w
        else:
            w = w * w * x
        print(w, bit)
        n = n // 2
    return w

a, b = 12, 1333

w1 = potega(a, b)
w2 = a**b
print(w1 == w2)
