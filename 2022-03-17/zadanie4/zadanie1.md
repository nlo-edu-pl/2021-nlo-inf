# Zadanie 1.1

## metoda zachłanna
```
23:
    pierwiastek z 23 --> [4..5]
    bierzemy 4
    4**2 => 16
    23 - 16 = 7
7:
    pierwiastek z 7 --> [2..3]
    bierzemy 2
    2**2 => 4
    7 - 4 = 3
    
3:
    pierwiastek z 3 --> [1..2]
    bierzemy 1
    1**2 => 1
    3 - 1 = 2

2:
    1 + 1
    
23: 4**2 + 2**2 + 1 + 1 + 1     (5 składników)
```
## metoda "prób i błędów"

```
23:
    spróbujmy 3
    3**2 = 9
    23 - 9 = 14
    14 - 9 = 5
    5 = 4 + 1
    
wynik:
    3**2 + 3**2 + 2**2 + 1      (4 składniki) 
```

## Zadanie 1.2

```python
def znajdz_najwiekszy_kwadrat_mniejszy_niz(n: int) -> int:
    liczba = 1
    while True:
        if liczba * liczba > n:
            return (liczba - 1)*(liczba - 1)
        liczba += 1

dl = 0
while n > 0: 
    n -= znajdz_najwiekszy_kwadrat_mniejszy_niz(n)
    dl += 1

print(f'{dl = }')
```