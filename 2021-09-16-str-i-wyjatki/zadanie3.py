with open("slowa.txt", encoding="utf8") as f:
    for linijka in f:
        slowo = linijka.strip()
        dlugosc = len(slowo)

        nazwapliku = f"slowa-{dlugosc}.txt"

        with open(nazwapliku, "a", encoding="utf8") as f2:
            f2.write(f"{slowo}\n")

        print(f"linijka={nazwapliku}")
