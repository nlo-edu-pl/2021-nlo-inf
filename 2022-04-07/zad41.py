nazwapliku = "2022-04-07/liczby.txt"

def odbicie(n):
    return int(str(n)[::-1])

liczby = []
with open(nazwapliku, 'r') as f:
    for linia in f:
        liczba = int(linia)
        liczby.append(liczba)

#print(liczby)
#print(len(liczby))

pary = []

for a in liczby:
    b = odbicie(a)
    czy_jest = b in liczby
    #print(a, b, czy_jest)
    para = [a, b]
    if a < 10:
        continue
    if len(str(a)) != len(str(b)):
        continue
    if a == b:
        continue
    if [b, a] in pary:
        continue
    if czy_jest:
        pary.append(para)

for x in pary:
    print(x)

print(len(pary))