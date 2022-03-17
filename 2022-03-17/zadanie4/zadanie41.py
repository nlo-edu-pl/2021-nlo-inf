wejscie = 'napisy.txt'
# wejscie = 'przyklad.txt'

licznik = 0

with open(wejscie, 'r') as plik:
    for linia in plik:
        for znak in linia:
            # print(f'{znak = }')
            #if znak in '0123456789':
            #    licznik += 1
            if znak.isnumeric():
                licznik += 1
        # print(f'{linia = }')

print(f'{licznik = }')

