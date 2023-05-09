plik = open("przyklad.txt", "r", encoding="utf-8")

linie = plik.readlines()

for linia in linie:
    linia_ = linia.split(" ")
    linia_set = list()
    for slowo in linia_:
        if slowo not in linia_set:
            linia_set.append(slowo)
    print(linia_set)
