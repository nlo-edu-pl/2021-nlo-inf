
try:
    with open("aaaa/report1.txt", "w") as f:
        f.write("Test 1")
except PermissionError:
    print("Brak praw dostępu")
except FileNotFoundError:
    print("Ścieżka nie istnieje")
except Exception:
    pass


import os

try:
    os.remove("plik.txt")
except:
    pass


if os.path.exists("plik.txt"):
    os.remove("plik.txt")

# https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use
