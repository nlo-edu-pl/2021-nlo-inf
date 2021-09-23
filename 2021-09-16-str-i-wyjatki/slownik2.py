oceny = {
    "matematyka": 4,
    "polski": 3,
    "historia": 2,
    "informatyka": 5
}

p = input("Podaj przedmiot: ")

if p in oceny:
    print(f"ocena to: {oceny[p]}")
else:
    print(f"brak oceny z {p}")
