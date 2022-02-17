# Logika

`True` == 1
`False` == 0

## Alternatywa

| p     | q     | p or q |
|-------|-------|--------|
| False | False | False  |
| False | True  | True   |
| True  | False | True   |
| True  | True  | True   |

### Przykład

```python
if a < 0 or a > 2.5:
    print("Nieprawidłowy wzrost")
```

### Notacja z języków C/C++/C#/Java/PHP i podobnych
```c 
if (a < 0 || a > 2.5) {
    napisz("Nieprawidłowy wzrost\n");
}
```

## Koniunkcja

| p     | q     | p and q |
|-------|-------|---------|
| False | False | False   |
| False | True  | False   |
| True  | False | False   |
| True  | True  | True    |

### Przykład

```python
if t > 0 and t < 100:
    print("Woda jest w stanie ciekłym")
```

### Notacja z języków C/C++/C#/Java/PHP i podobnych
```c 
if (t > 0 && t < 100) {
    napisz("Woda w stanie ciekłym\n");
}
```

# Operacje bitowe

## bitowe OR

```
    1100 0001       193
    1000 0110       134
    -------------------
    1100 0111       199
```

### Python
```python
a = 193
b = 134
c = a | b

print(c)    # wynik: 199
```

## bitowe AND
```
    1100 0001       193
    1000 0110       134
    -------------------
    1000 0000       128
```

### Python
```python
a = 193
b = 134
c = a & b

print(c)    # wynik: 128
```


## bitowe XOR
exclusive or, różnica symetryczna
```
    1100 0001       193
    1000 0110       134
    -------------------
    0100 0111        71
```

### Python
```python
a = 193
b = 134
c = a ^ b

print(c)    # wynik: 71
```











