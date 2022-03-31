import zad4


def polacz(a: int, b: int) -> int:
    return polacz_str(a, b)

def polacz_str(a: int, b: int) -> int:
    return int(f'{a}{b}')

def gcd(a: int, b: int) -> int:
    if a < b:
        return gcd(b, a)
    if a%b == 0:
        return b
    return gcd(b, a%b)

pary = zad4.wczytaj_pary()
polaczone = []

for a, b in pary:
    polaczona = polacz(a, b)
    polaczone.append(polaczona)

global_gcd = polaczone[0]

for p in polaczone:
    print(f'{p = } {global_gcd = }')
    global_gcd = gcd(p, global_gcd)
    
