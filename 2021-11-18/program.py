import funkcje

punkty = []
with open("2021-11-18/punkty.txt", "r") as f:
    for linia in f:
        x, y = linia.strip().split(",")
        x = float(x)
        y = float(y)
        punkt = (x, y)
        punkty.append(punkt)

dl = funkcje.dlugosc_sciezki(punkty)
print(dl)
