# Napisz funkcję odbierającą w postaci *args dowolną ilość elementów i zwracającą ich iloczyn.


def zad4(**kwargs):
    iloczyn = 1

    for value in kwargs.values():
        iloczyn *= value
    return iloczyn


print(zad4(a=3,b=4))