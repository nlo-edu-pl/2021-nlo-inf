import sqlite3

db = sqlite3.connect('zad6.db')

db.execute("""
    Create Temporary View czasy As
    Select 
        id_ucznia,
        Substr(czas_logowania, 1, 2) * 3600
        + Substr(czas_logowania, 4, 2) * 60
        + Substr(czas_logowania, 7, 2)
        As login,
        Substr(czas_zapisu, 1, 2) * 3600
        + Substr(czas_zapisu, 4, 2) * 60
        + Substr(czas_zapisu, 7, 2)
        As zapis
    From "dane logowania";
""")

print("Zad 66")
sql = """
    Select
        *,
        (zapis - login) - 3600 As przekroczenie
    From czasy
    Join uczniowie Using (id_ucznia)
    Where zapis - login > 3600
    Order By przekroczenie Desc;
"""

for r in db.execute(sql):
    print(r)
