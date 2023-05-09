bill_items = [
   ['Tom', 'Calamari', 6.00],
   ['Tom', 'American Hot', 11.50],
   ['Tom', 'Chocolate Fudge Cake', 4.45],
   ['Clare', 'Bruschetta Originale', 5.35],
   ['Clare', 'Fiorentina', 10.65],
   ['Clare', 'Tiramisu', 4.90],
   ['Rich', 'Bruschetta Originale', 5.35],
   ['Rich', 'La Reine', 10.65],
   ['Rich', 'Honeycomb Cream Slice', 4.90],
   ['Rosie', 'Garlic Bread', 4.35],
   ['Rosie', 'Veneziana', 9.40],
   ['Rosie', 'Tiramisu', 4.90],
]

zestawienie = {}
lista_empty = []
for item in bill_items:
    if item[0] not in zestawienie.keys():
        zestawienie[item[0]] = {"potrawy": list(), "cena": 0}
    if item[0] in zestawienie.keys():
        zestawienie[item[0]]['potrawy'].append(item[1])
        zestawienie[item[0]]['cena'] += item[2]

print(zestawienie)
