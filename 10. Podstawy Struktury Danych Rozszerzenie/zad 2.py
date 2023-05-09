from random import randint

lista = []
for i in range(15):
    lista.append(randint(15, 120))

lista2 = lista

print(lista)
for i in lista2:
    if i % 2 == 0:
        lista.remove(i)

print(lista)
