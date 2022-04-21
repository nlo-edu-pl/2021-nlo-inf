import ipaddress

# ip = input("Podaj adres IP: ")
# try:
#     ip3 = ipaddress.IPv4Address(ip)
# except ipaddress.AddressValueError:
#     print("Nieprawidłowy adres")

ip1 = ipaddress.IPv4Address('12.34.12.11')
maska = ipaddress.IPv4Address('255.255.255.0')

siec = int(ip1) & int(maska)

print(ip1)
print(maska)
print(siec)

for host in range(1,17):
    print(siec + host)


# ip2 = ipaddress.IPv4Address(203557906)

# siec1 = ipaddress.IPv4Network('12.34.0.0/16')
# siec2 = ipaddress.IPv4Network('129.34.0.0/24')

# print(ip1, ip2, siec1, siec2)

# print(ip2 in siec1)
# print(ip1 in siec2)

# ip1_liczba = int(ip1)

# print(ip1_liczba)
