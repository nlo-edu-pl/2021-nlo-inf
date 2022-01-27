# PIERWSZY SPOSÓB

liczby = [5, 67, 100, 1, 30, 45]

liczby2 = sorted(liczby)

print(f'{liczby = }')
print(f'{liczby2 = }')

# wniosek: pierwotna lista (liczby) nie została zmodyfikowana

# DRUGI SPOSÓB

liczby.sort()

print(f'{liczby = }')

# wniosek: pierwotna lista (liczby) została zmodyfikowana (in-place)
