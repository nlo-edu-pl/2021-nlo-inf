import math

# bez anotacji typów (standardowo)
# def ile_porcji(dost_m, dost_z, dost_s):

# z anotacją typów (opcjonalne w pythonie)
def ile_porcji(dost_m: float, dost_z: float, dost_s: float) -> int:
    ile_p_m = math.floor(dost_m / 0.4)
    ile_p_z = math.floor(dost_z / 0.3)
    ile_p_s = math.floor(dost_s / 0.2)
    return min([ile_p_m, ile_p_z, ile_p_s])

m = 21
z = 1000.3
s = 12.3

print(ile_porcji(m, z, s))
