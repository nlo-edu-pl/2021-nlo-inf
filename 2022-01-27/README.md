# Algorytmy sortowania

## Bubble sort (bąbelkowe)

```python
def bubble_sort(tablica):
    "Sortowanie Bubble sort in-place"
    dlugosc = len(tablica)
    for j in range(dlugosc - 1):
        for i in range(dlugosc - 1 - j):
            a, b = tablica[i:i+2]
            if b < a:  # trzeba zamienić
                tablica[i:i+2] = b, a
```

## Insertion sort (przez wstawianie)

### Wersja funkcyjna

```python
def insertion_sort(tablica):
    "Sortowanie Insertion sort (funkcyjne, z użyciem list)"
    nowa = []
    for wartosc in tablica:
        pozycja = len(nowa)  # na koniec
        for p, x in enumerate(nowa):
            if x > wartosc: # trzeba wstawic przed nim
                pozycja = p
                break
        nowa.insert(pozycja, wartosc)
    return nowa
```

### Wersja in-place

```python
def insertion_sort(tablica):
    "Insertion sort in-place"
    for i in range(1, len(tablica)):
        j = i
        while j > 0 and tablica[j-1] > tablica[j]:
            tablica[j-1], tablica[j] = tablica[j], tablica[j-1]
            j -= 1
```

## Selection sort (przez wybór)

```python
def selection_sort(tablica):
    "Insertion sort in-place"
    for p in range(len(tablica)):
        pozycja_min = p
        for i in range(p, len(tablica)):
            if tablica[i] < tablica[pozycja_min]:
                pozycja_min = i
        tablica[p], tablica[pozycja_min] = tablica[pozycja_min], tablica[p] # zamiana elementów miejscami
```

## Merge sort (przez scalanie)

### Wersja rekurencyjna

```python
def merge(tablica_a, tablica_b):
    wynik = []
    while len(tablica_a) > 0 and len(tablica_b) > 0:
        if tablica_a[0] > tablica_b[0]:
            elem = tablica_b.pop(0)
        else:
            elem = tablica_a.pop(0)
        wynik.append(elem)
    wynik.extend(tablica_a + tablica_b)
    return wynik

def merge_sort(tablica):
    dlugosc = len(tablica)
    if dlugosc <= 1:
        return tablica
    a, b = tablica[0:dlugosc//2], tablica[dlugosc//2:]
    return merge(merge_sort(a), merge_sort(b))
```

### Wersja bez rekurencji

```python
def merge(tablica_a, tablica_b):
    wynik = []
    while len(tablica_a) > 0 and len(tablica_b) > 0:
        if tablica_a[0] > tablica_b[0]:
            elem = tablica_b.pop(0)
        else:
            elem = tablica_a.pop(0)
        wynik.append(elem)
    wynik.extend(tablica_a + tablica_b)
    return wynik

def merge_sort(tablica):
    kolejka = []
    for element in tablica:
        kolejka.append([element])
    while len(kolejka) > 1:
        a = kolejka.pop(0)
        b = kolejka.pop(0)
        kolejka.append(merge(a, b))
    return kolejka.pop()
```