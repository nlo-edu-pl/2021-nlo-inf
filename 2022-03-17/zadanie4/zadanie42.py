wejscie = 'napisy.txt'
# wejscie = 'przyklad.txt'
haslo = ''
with open(wejscie, 'r') as plik:
    for numer, linia in enumerate(plik):
        numer += 1
        if numer % 20 == 0:
            pozycja = numer // 20
            znak = linia[pozycja-1]
            haslo += znak
            print(f'{numer = } {pozycja = } {znak = } {linia = }')

print(f'{haslo = }')
