nazwapliku = "2022-04-07/liczby.txt"

def czy_pierwsza(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
        if i * i > n:
            break
    return True

def odbicie(n):
    return int(str(n)[::-1])

liczby = []
with open(nazwapliku, 'r') as f:
    for linia in f:
        liczba = int(linia)
        liczby.append(liczba)

pary = []
for a in liczby:
    if a < 10:
        continue
    b = odbicie(a)
    if czy_pierwsza(a) and czy_pierwsza(b):
        para = [a, b]
        para.sort()
        if para in pary:
            continue
        pary.append(para)
pary.sort()

print(pary)
print(len(pary))