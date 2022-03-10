def wspak2(napis: str) -> str:
    """Funkcja zwracająca napis wspak"""
    return napis[::-1]

def wspak(napis: str) -> str:
    nowe_slowo = ''
    for i in range(len(napis), 0, -1):
        nowe_slowo += napis[i-1]
    return nowe_slowo

def wspak_rek(napis: str) -> str:
    if len(napis) <= 1:
        return napis
    return wspak_rek(napis[1:]) + napis[0]

for x in ['wenus', 'kot', 'kobyłamamałybok']:
    print(wspak_rek(x))

assert wspak("wenus") == "sunew"
assert wspak("kot") == "tok"
assert wspak("zakopanenapokaz") == "zakopanenapokaz"
