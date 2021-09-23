oceny = {
    "matematyka": 4,
    "polski": 3,
    "historia": 2,
    "informatyka": 5
}

p = input("Podaj przedmiot: ")

try:
    print(f"ocena to: {oceny[p]}")
except KeyError:
    print("Brak oceny")

