LISTA = ['zielony', 'czerwony', 'niebieski', 'czarny', 'fioletowy', 'granatowy', 'niebieski',
         'czarny', 'czarny', 'zielony', 'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony', 'czerwony']
print(LISTA)
zbior = set(LISTA)
print(zbior)

print(len(LISTA))
print(len(zbior))
for i in zbior:
    print(i)

zbior.remove("zielony")
print(len(zbior))
zbior.add("ujowy")
print(len(zbior))
