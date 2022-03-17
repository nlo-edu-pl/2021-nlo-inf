wejscie = 'napisy.txt'
# wejscie = 'przyklad.txt'


def czy_palindrom(napis: str) -> bool:
    return napis == napis[::-1]


def czy_prawie_palindrom2(napis: str) -> bool:
    pierwsza = napis[0]
    ostatnia = napis[-1]
    return czy_palindrom(napis + pierwsza) or czy_palindrom(ostatnia + napis)


def czy_prawie_palindrom(napis: str) -> bool:
    bez_pierwszej = napis[1:]
    bez_ostatniej = napis[:-1]
    return czy_palindrom(bez_pierwszej) or czy_palindrom(bez_ostatniej)


def zrob_palindrom(napis: str) -> str:
    mozliwosc1 = napis[1:]
    mozliwosc2 = napis[:-1]
    if czy_palindrom(mozliwosc1):
        return mozliwosc1
    else:
        return mozliwosc2


haslo = ''

with open(wejscie) as plik:
    for linia in plik:
        linia = linia.strip()
        if not czy_prawie_palindrom(linia):
            continue
        pal = zrob_palindrom(linia)
        srodkowa_litera = pal[len(pal)//2]
        haslo += srodkowa_litera
        print(f'{linia = } {pal = } {srodkowa_litera =}')

print(f'{haslo = }')