# Zadania na dziś

Rozwiązania wysłać na maila nauczyciela do dnia 2021-11-17 godz 23:59.

## Generator danych

Napisać program, który:
1. wczyta z pliku tekstowego `parametry.txt` trzy liczby:
  - liczbę punktów (`n: int`)
  - szerokość (`w: int` lub `float`)
  - wysokość (`h: int` lub `float`)
2. Wygeneruje losowo `n` współrzędnych z zakresu od `(0, 0)` do `(w, h)` i zapisze do pliku `punkty.txt`

### Przykład

Dla pliku wejściowego (`parametry.txt`):
```
5
10
20
```

Plik wyjściowy (`punkty.txt`) może wyglądać np. tak:
```
7.85,5.14
9.15,13.40
7.28,4.56
4.00,11.72
2.15,1.88
```

### Podpowiedź

Użyć funkcji `uniform` z modułu `random`

```python
import random

x = random.uniform(0, 30)

# Wyświetli losową liczbę typu float z zakresu od 0.0 do 30.0
print(f"{x}")
```

## Funkcje

### `odleglosc()`
```python
def odleglosc(p1: tuple, p2: tuple) -> float:
   ...
```

1. Napisać funkcję `odleglosc()`, która oblicza odległość dwoch punktów na płaszczyźnie.
2. Stworzyć do niej proste testy
3. Podpowiedź: parametrami funkcji są dwuelementowe krotki zawierające współrzędne `x` i `y` punktów. 

### `dlugosc_sciezki()`
```python
def dlugosc_sciezki(sciezka: list) -> float:
   ...
```

1. Napisać funkcję `dlugosc_sciezki()`, która oblicza długość ścieżki przechodzącej przez kolejne punkty.
2. Swtorzyć do niej proste testy.
3. Podpowiedź: parametrem funkcji jest lista zawierająca punkty

## Program

Napisać program wczytujący kolejne punkty ścieżki z pliku `punkty.txt` i podający długość ścieżki.
