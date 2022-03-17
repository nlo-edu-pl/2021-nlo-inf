def znajdz_najwiekszy_kwadrat_mniejszy_niz(n: int) -> int:
    liczba = 1
    while True:
        if liczba * liczba > n:
            print(f'{liczba-1}**2')
            return (liczba - 1)*(liczba - 1)
        liczba += 1

n = 12

dl = 0
while n > 0: 
    n -= znajdz_najwiekszy_kwadrat_mniejszy_niz(n)
    dl += 1

print(f'{dl = }')