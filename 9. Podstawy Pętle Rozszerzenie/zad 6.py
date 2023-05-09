INPUT = '1235555'

slownik_ile = dict()

for znak in INPUT:
    if znak not in slownik_ile.keys():
        slownik_ile[znak] = 1
    else:
        slownik_ile[znak] += 1
print(slownik_ile)
