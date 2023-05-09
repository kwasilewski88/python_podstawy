zamowienia = {"Klient_1335": {"nazwa_potrawy": "rosół", "ocena": 5, "rachunek": 20.0},
              "Klient_222": {"nazwa_deseru": "lody waniliowe", "rachunek": 5.0}}


for key, value in zamowienia.items():
    print(key)
    for key_, value_ in value.items():
        print(key_, value_)
