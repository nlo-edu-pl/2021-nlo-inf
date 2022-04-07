# Zad 2.3

```python
def wynik(n):
    #      0: 1:  2:
    tab = [2, -1, 1]

    if n <= 3:  # n=1, 2 lub 3
        return tab[n-1]

    for i in range(4, n+1):      # 1, 2, 3, ..., n
#        nowy = sum(tab)
        nowy = tab[0] + tab[1] + tab[2]
        a, b, c = tab
        tab = [b, c, nowy]
#        tab = tab[1:] + [nowy]
    return nowy

```