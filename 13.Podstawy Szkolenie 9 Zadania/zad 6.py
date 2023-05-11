# Zrób system, który obsługiwał będzie określone zamówienia.
# W programie istnieć będą 2 klasy: Manager oraz Order.
# W Managerze ma się znajdować słownik zamówień, w którym kluczem będzie obiekt zamówienia,
# a wartością jego ilość na stanie.
# W klasie Order natomiast mają znajdować się takie pola jak: id, nazwa, cena.
#
# Funkcjonalność programu to:
# - dodawanie nowego zamówienia do słownika
# (jeżeli dodawać będziemy obiekt, którego id znajduje się już w słowniku,
# to nie będziemy dodawali nowej pary do dicta,
# ale zwiększali ilość danego obiektu w słowniku (zwiększali odpowiednią wartość w słowniku)).
# - usuwanie o 1 zamówienia ze słownika o określonym id

class Manager:
    def __init__(self):
        self.orders = {}

    def add_order(self, order, amount):
        if self.orders == {}:
            self.orders[order] = amount
        else:
            list_id = []
            for key in self.orders.keys():
                list_id.append(key.get_id())
            if order.get_id() in list_id:
                for key, value in self.orders.items():
                    if order.get_id() == key.get_id():
                        self.orders[key] += amount
            else:
                self.orders[order] = amount

    def sell_order(self, sell):
        if self.orders == {}:
            print("nie ma z czego sprzedawac")
        else:
            list_id = []
            for key in self.orders.keys():
                list_id.append(key.get_id())
            if sell.get_id() not in list_id:
                print("nie ma takiego produktu dostepnego")
            else:
                for key, value in self.orders.items():
                    if sell.get_id() == key.get_id():
                        if self.orders[key] == 0:
                            print("nic nie zostalo na stanie")
                        else:
                            self.orders[key] -= 1

    def get_info(self):
        for key, value in self.orders.items():
            print(key.get_info(), value)


class Order:
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def get_id(self):
        return self.id

    def get_info(self):
        return self.id, self.nazwa, self.cena


order1 = Order(1, "lalka", 100)
order2 = Order(1, "lalka", 100)
order3 = Order(2, "pies", 1000)
order4 = Order(3, "kot", 1000)

manager1 = Manager()
manager1.get_info()
manager1.add_order(order1, 3)
manager1.get_info()
manager1.add_order(order1, 5)
manager1.get_info()
manager1.add_order(order2, 10)
manager1.get_info()
manager1.add_order(order3, 1)
manager1.get_info()
manager1.sell_order(order4)
manager1.get_info()
manager1.sell_order(order3)
manager1.get_info()
manager1.sell_order(order3)
manager1.get_info()
