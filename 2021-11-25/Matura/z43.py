import z4

najdluzszy = 0

with open("liczby.txt") as f:
    dlugosc = 0
    poprzednia = -999
    poprzednia_czy_wesola = False
    for l in f:
        l = int(l)
        czy_wesola = z4.czy_wesola(l)

        if poprzednia >= 0:
            if poprzednia < l and poprzednia_czy_wesola and czy_wesola:
                dlugosc += 1
                if dlugosc > najdluzszy:
                    najdluzszy = dlugosc
            else:
                dlugosc = 0
        
        print(f"{l:20} {czy_wesola:6}  {poprzednia:20} {poprzednia_czy_wesola:6} {'@' * dlugosc}")
        poprzednia = l
        poprzednia_czy_wesola = czy_wesola

print(f"{najdluzszy=}")

