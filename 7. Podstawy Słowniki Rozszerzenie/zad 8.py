slownik = {
    "V": "S001",
    "VI": "S002",
    "VII": "S001",
    "VIII": "S005",
    "IX": "S005",
    "X": "S009",
    "XI": "S007"
}

zbior = set()
print(zbior)

lista = []
slownik_licz = {}
for word in slownik.values():
    if word not in slownik_licz:
        slownik_licz[word] = 1
    else:
        slownik_licz[word] += 1

print(slownik_licz)
for key, value in slownik_licz.items():
    if value == 1:
        zbior.add(key)
print(zbior)
