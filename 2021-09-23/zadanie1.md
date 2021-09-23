# Zadanie 1.2

```
funkcja F(T,x) 
    p ← 1 
    k ← n 
    dopóki p <= k powtarzaj: 
        s ← (p+k) div 2 
        jeśli T[s] = x to 
            wynikiem jest prawda 
            zakończ działanie funkcji
        w przeciwnym razie 
            jeśli T[s] < x to p ← s+1 
            w przeciwnym razie k ← s-1 
    wynikiem jest fałsz
```

```
T =  [3; 5; 7; 8; 9; 13; 33; 37; 40; 43]
x = 7
n = 10
```

|  p |  k |  s | T[s] | x  | T[s]=x | T[s]<x |
|----|----|----|------|----|--------|--------|
|  1 | 10 |  5 |  9   |  7 | fałsz  | fałsz  |
|  1 |  4 |  2 |  5   |  7 | fałsz  | prawda |
|  3 |  4 |  3 |  7   |  7 | prawda | ---    |

Pętla wykonała się 3 razy.
Liczba modyfikacji:
`p`: 1
`k`: 1



