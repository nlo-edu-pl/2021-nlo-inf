def czy_anagram(slowo1: str, slowo2: str) -> bool:
    return sorted(slowo1) == sorted(slowo2)


pary = [
    ["matura", "trauma"],
    ["masło", "słoma"],
    ["kot", "pies"]
]

for x1, x2 in pary:
    print(f"{x1} {x2} {czy_anagram(x1, x2)}")