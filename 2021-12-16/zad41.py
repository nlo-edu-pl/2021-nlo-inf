import zad4

liczby_z_najdluzszym_cyklem = []

for i in range(1, 1000+1):
    if zad4.czy_wesola(i):
        ile = len(zad4.kolejne_wesole(i))
        if ile == 7:
            liczby_z_najdluzszym_cyklem.append(i)
        print(f"{i}: {ile}")

print(liczby_z_najdluzszym_cyklem)
