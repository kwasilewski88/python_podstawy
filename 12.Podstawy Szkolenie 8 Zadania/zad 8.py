import json


def zad8(**kwargs):
    slownik = dict()
    for key in kwargs:
        print(key, kwargs[key])
        slownik[kwargs[key]] = key
    print(slownik)

    with open('output.json', 'w') as outfile:
        json.dump(slownik, outfile)


zad8(lala=5, jak=7)
