nazwapliku = "2022-04-07/liczby.txt"

def gcd(a, b):
    if b == 0:
        return a
    print(f"GCD({a}, {b}")
    return gcd(b, a%b)


def odbicie(n):
    return int(str(n)[::-1])

def polacz(n1, n2):
    return int(str(n1) + str(n2))

liczby = []
with open(nazwapliku, 'r') as f:
    for linia in f:
        liczba = int(linia)
        liczby.append(liczba)

for a in liczby:
    b = odbicie(a)
    c = polacz(a, b)
    print(a, b, c)
