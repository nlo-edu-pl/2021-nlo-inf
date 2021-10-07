*imię, nazwisko, klasa*

# Kartkówka 2021-10-07

## Zadanie 1

Dla poniższych słownych opisów działania funkcji napisać ich **sygnaturę** w języku *python*.
Podać typy parametrów i typ wartości zwracanej. (Niektóre przypadki mogą mieć kilka rozwiązań)

**Nie chodzi tu o implementację funkcji!**

### Przykład
Dla podanej pary liczb całkowitych funkcja zwraca informację, czy ich iloczyn jest podzielny przez 7.

```python
def czy_iloczyn_podzielny_przez_siedem(a: int, b: int) -> bool:
   ...

# parametry:
#   a - pierwsza liczba (int)
#   b - druga liczba (int)
# typ zwracany: bool
```
### Do zrobienia
1. Dla podanych długości boków trójkąta funkcja podaje, czy taki trójkąt może istnieć na płaszczyźnie.
2. Dla podanych długości boków trójkąta funkcja podaje, czy jest to trójkąt prostokątny.
3. Dla podanego dnia, miesiąca i roku funkcje zwraca dzień tygodnia.
4. Dla podanej liczby głosów wielu list wyborczych oraz liczby mandatów w danym okręgu, funkcja zwraca informację o liczbie mandatów poszczególnych list. (wyliczoną np. metodą d'Hondta)
5. Dla podanego napisu, funkcja zwraca liczbę samogłosek.
6. Dla podanego napisu, funkcja zwraca stosunek liczby znaków interpunkcyjnych do wszystkich znaków.
7. Dla podanej masy i objętości próbki zwraca gęstość substancji.
8. Dla podanego pierwiastka chemicznego zwraca jego masę atomową.
9. Dla podanej liczby atomowej zwraca nazwę pierwiastka.
10. Dla podanego wzoru chemicznego np. `H2SO4` zwraca masę molową.
11. Dla podanego wzrostu i waga zwraca BMI.
12. Dla podanej ceny brutto i stawki VAT (określonej kategorią: `A` - 23%, `B` - 8% itd) zwraca cenę netto.
13. Dla podanego dnia i miesiąca zwraca imiona osób obchodzących tego dnia imieniny.

## Zadanie 2
Które z powyższych funkcji mogłyby zgłaszać wyjątki i w jakim wypadku?

