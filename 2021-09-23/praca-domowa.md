Zaimplementować algorytm z zadania 1 z arkusza maturalnego czerwiec 2018.

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
            jeśli T[s] < x to
                p ← s+1 
            w przeciwnym razie
                k ← s-1 
    wynikiem jest fałsz 
```

Napisać proste programiki prezentujące rozwiązania zadań od 1.1 do 1.3.

Zadanie 2 z arkusza maturalnego.
