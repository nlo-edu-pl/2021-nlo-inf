def Frek(n):
    if n == 1: return 1
    if n == 2: return 1
    return Frek(n-1) + Frek(n-2)

def Frek2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n % 2 == 0:
        k = n // 2
        return Frek2(k+1)**2 - Frek2(k-1)**2
    else:
        k = (n+1)//2
        return Frek2(k)**2 + Frek2(k-1)**2

def F(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

for i in range(1, 30):
    print(f"{i=} {F(i)=} {Frek(i)=} {Frek2(i)=}")

# for i in range(3, 100):
#     x = F(i+1)
#     y = F(i)
#     fi = x/y
#     print(f"{fi=}")


