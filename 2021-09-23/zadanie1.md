# Zadanie 1

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

## Zadanie 1.1

### Dla `x = 7`

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

### Dla `x = 43`

```
T =  [3; 5; 7; 8; 9; 13; 33; 37; 40; 43]
x = 7
n = 10
```

|  p |  k |  s | T[s] | x  | T[s]=x | T[s]<x |
|----|----|----|------|----|--------|--------|
|  1 | 10 |  5 |  9   | 43 | fałsz  | prawda |
|  6 | 10 |  8 | 37   | 43 | fałsz  | prawda |
|  9 | 10 |  9 | 40   | 43 | fałsz  | prawda |
| 10 | 10 | 10 | 43   | 43 | prawda | ---    |

Pętla wykonała się 4 razy.
Liczba modyfikacji:
`p`: 3
`k`: 0

## Zadanie 1.2

```
T = [10, 20, 30, 40, ... 990, 1000]
n = 100
x = 2021
```

|  p |   k |  s | T[s] | x  | T[s]=x | T[s]<x |
|----|-----|----|------|----|--------|--------|
|  1 | 100 |  50| 500  |2021| fałsz  | prawda |
| 51 | 100 |  75| 750  |2021| fałsz  | prawda |
| 76 | 100 |  88| 880  |2021| fałsz  | prawda |
| 89 | 100 |  94| 940  |2021| fałsz  | prawda |
| 95 | 100 |  97| 970  |2021| fałsz  | prawda |
| 98 | 100 |  99| 990  |2021| fałsz  | prawda |
|100 | 100 | 100|1000  |2021| fałsz  | prawda |
|101 | 100 | ---|---|  |--- | ---    | ---    |

Warunek był spełniony 7 razy.

