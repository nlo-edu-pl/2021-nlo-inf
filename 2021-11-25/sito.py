MAX = 10000
Sito = [True] * MAX

for p in range(2, MAX):
    if Sito[p] == True:
        z = p * p
        while z < MAX:
            Sito[z] = False
            z += p

for i in range(2, MAX):
    if Sito[i]:
        print(i)

for i in range(2, MAX):
    if Sito[i] and Sito[i+2] and Sito[i+6] and Sito[i+8]:
        print(i, i+2, i+6, i+8)