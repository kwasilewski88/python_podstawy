lista1 = ["abc", "def", "ghi", "jkl"]
lista2 = [1, 2, 3, 4, 5]
lista3 = ["xyz", 1, '2']

print(lista1)
print(lista2)
print(lista3)

print(lista1[0], lista1[3])
lista2[1] = lista3[1]
lista3[2] = "dupa"

print(lista1)
print(lista2)
print(lista3)


lista1.append("słowo")
lista1.pop(1)

print(lista1)
print(lista2)
print(lista3)

print(len(lista3))

lista1.extend(lista3)
print(lista1)
