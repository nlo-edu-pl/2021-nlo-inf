# Zadanie 3.1
```

((not a) and b) or (a and (not b)) 



a   b       not a       (not a) and b       (not b)     (a and !b)      X or Y
0   0       1           0                   1           0               0
1   0       0           0                   1           1               1   
0   1       1           1                   0           0               1
1   1       0           0                   0           0               0



Odpowiedzi:

W(0, 0) == 1     FAŁSZ
W(1, 0) == 1     PRAWDA
W(0, 1) == 0     FAŁSZ
W(1, 1) == 0     PRAWDA
```

# Zadanie 3.2

```
(10101)2 + (101011)2 = (111111)     FAŁSZ, BO nieparz + nieparz => parz

(A)16 + (B)16 = (F)16
10 + 11 => 21
            21 dec => 15 hex !=         FAŁSZ

(12)8 + (12)8 = (14)16      PRAWDA

001 010  + 001 010  => 010 100
                       01 0100
                        1    4 HEX

(123)10 = (1111101)2    FAŁSZ
