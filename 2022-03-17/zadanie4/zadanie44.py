wejscie = 'napisy.txt'
# wejscie = 'przyklad.txt'

def oczysc(linia: str) -> str:
    nowa_linia = ''
    for znak in linia:
        if znak.isnumeric():
            nowa_linia += znak
    return nowa_linia

haslo = ''
koniec = False

with open(wejscie) as plik:
    for linia in plik:
        linia = oczysc(linia)
        if linia == '':
            continue
        if len(linia) % 2 == 1:
            linia = linia[:-1]
        for poz in range(0, len(linia), 2):
            dwuznak = linia[poz:poz+2]
            liczba = int(dwuznak)
            if liczba < 65 or liczba > 90:
                continue
            litera = chr(liczba)
            haslo += litera
            if haslo.endswith('XXX'):
                koniec = True
                break
            #print(f'{litera = }')
        if koniec:
            break
        #print(f'{linia = }')

print(f'{haslo = }')