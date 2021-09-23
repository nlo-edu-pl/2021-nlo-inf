# Funkcje do operacji na nazwach plików i ścieżkach

## Wczytywanie zawartości katalogu

```python
import os

# katalog bieżący
print(os.listdir())
```
Dowolny katalog:

```python
import os

# katalog C:\Windows
print(os.listdir('C:/Windows'))
```

## Wczytywanie listy plików pasujących do maski
```python
import glob

print(glob.glob('*.png'))
```

## Operacje na ścieżkach

### Tylko nazwa katalogu
```python
import os

x = 'C:/Windows/System32/drivers/etc/hosts'
os.path.dirname(x)
```

### Tylko nazwa pliku
```python
import os

x = 'C:/Windows/System32/drivers/etc/hosts'
os.path.basename(x)
```

### Inne

```
os.path.realpath()
```
