plik = open("przyklad.txt", "r", encoding="utf-8")
linie = plik.readlines()

for i in range(1, len(linie)):
    if (i+1) % 2 == 0:
        print(linie[i])


plik.close()
