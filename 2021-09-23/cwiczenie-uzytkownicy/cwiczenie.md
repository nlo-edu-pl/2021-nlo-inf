Stworzyć program, który:
- wczyta z plików wejściowych imiona i nazwiska uczniów, podzielone wg klas
- zapisze do pliku wyjściowego listę kont do założenia:

Format pliku wyjściowego:

```
Jan;Kowalski;jan.kowalski;jan.kowalski@nlo.edu.pl;1E
Michał;Jóźwik;michal.jozwik;michal.jozwik@nlo.edu.pl;1F
```

```python

with open("plik1.txt") as f:
    for linia in f:
        ...
```

