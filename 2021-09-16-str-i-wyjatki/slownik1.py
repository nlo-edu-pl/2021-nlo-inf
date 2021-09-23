oceny = {
    "matematyka": 4,
    "polski": 3,
    "historia": 2,
    "informatyka": 5
}

p = input("Podaj przedmiot: ")

for przedmiot in oceny:
    # print(przedmiot)
    if p == przedmiot:
        print(f"ocena to: {oceny[p]}")
        break
else:
    print(f"brak oceny z {p}")

# Ocena z tego przedmiotu to: X
# albo: brak oceny z tego przedmiotu
