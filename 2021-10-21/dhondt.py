# import os
# os.chdir(os.path.dirname(__file__))

with open("2021-10-21/wybory1.txt") as f:
    for linia in f:
        komitet, glosy = linia.split(":")
        glosy = int(glosy)
        print(komitet)
        print(glosy // 1000)


# partia ABC = 199999
# partia ... = ....
