from random import randint

wynik = [12, 1, 45, 76, 50, 23]

for i in range(len(wynik)):
    if wynik[i] > 49:
        print("liczba spoza zakresu")
        wynik[i] = randint(1, 49)

print(wynik)
