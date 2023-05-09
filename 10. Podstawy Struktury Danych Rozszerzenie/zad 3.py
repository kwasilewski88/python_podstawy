slownik = {'a': 3,
           'b': 1,
           'c': 10,
           'd': 15,
           'e': 20}

slownik_nowy = {}
for key, value in slownik.items():
    slownik_nowy[value] = key

print(slownik_nowy)
