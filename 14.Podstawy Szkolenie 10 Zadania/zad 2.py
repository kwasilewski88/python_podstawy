# Zaprojektuj z użyciem koncepcji dziedziczenia hierarchię klas opisujących pojazdy komunikacji
# miejskiej. Wyraź w tej hierarchii następujące fakty:
#
# 1. wszystkie pojazdy komunikacji miejskiej (k. m.) są poj vazdami,
# 2. komunikacja miejska używa tramwajów i autobusów,
# 3. pojazdy są garażowane w zajezdniach, odpowiednio tramwajowych i autobusowych,
# 4. każdy pojazd zna swoją szybkość maksymalną,
# 5. każdy pojazd k. m. zna swój numer,
# 6. każdy pojazd k. m. zna swoją zajezdnię,
# 7. każdy tramwaj jest zestawem 1 do 3 wagonów (i wie, z ilu wagonów się składa),
# 8. każdy autobus wie, ile zużył paliwa w bieżącym miesiącu,
# 9. każda zajezdnia wie, jakie pojazdy do niej należą,
# 10. każda zajezdnia ma nazwę.
#
# Każdy pojazd powinien mieć możliwość podawania swojego opisu w postaci napisu.
# Opis ma zawierać wszystkie informacje, które zna dany pojazd (np. numer, czy szybkość maksymalną).
# Opis zajezdni to nazwa zajezdni, jej typ i opisy poszczególnych pojazdów.
# Zajezdnia autobusowa podaje dodatkowo sumaryczne zużycie paliwa w bieżącym miesiącu,
# a tramwajowa ogólną liczbę wagonów.
# Do prezentowania informacji o obiekcie, wykorzystaj metodę specjalną __str__().!!!!
#
# Napisz program, który utworzy kilka obiektów reprezentujących wszystkie pojazdy i dwie zajezdnie
# (autobusową i tramwajową), przydzieli pojazdy do zajezdni,
# a następnie wypisze opis obu zajezdni.


class Vehicle:
    def __init__(self, max_speed, number, depot):
        self.max_speed = max_speed
        self.number = number
        self.depot = depot
        depot.add_vehicle(self)

    def get_description(self):
        print(f"predkosc maksymalna to {self.max_speed} ,"
              f"numer to {self.number} , "
              f"zajezdnia to {self.depot.name}")


class Tram(Vehicle):
    def __init__(self, max_speed, number, depot, cars):
        super().__init__(max_speed, number, depot)
        self.cars = cars

    def get_cars(self):
        return self.cars

    def get_description(self):
        super().get_description()
        print(f"ilosc wagonow {self.cars}")


class Bus(Vehicle):
    def __init__(self, max_speed, number, depot, used_fuel):
        super().__init__(max_speed, number, depot)
        self.used_fuel = used_fuel

    def get_used_fuel(self):
        return self.used_fuel

    def get_description(self):
        super().get_description()
        print(f"zuzycie paliwa to  {self.used_fuel }")


class Depot:
    def __init__(self, name):
        self.name = name
        self.list_vehicles = []

    def add_vehicle(self, vehicle):
        self.list_vehicles.append(vehicle)

    def get_vehicles(self):
        return self.list_vehicles

    def get_description(self):
        print(f"nazwa to {self.name} ")
        for vehicle in self.list_vehicles:
            vehicle.get_description()


class DepotTram(Depot):
    def __init__(self, name):
        super().__init__(name)

    def get_description(self):
        super().get_description()
        super().get_description()
        print("typ to  tramwajowa")
        suma = 0
        for vehicle in self.list_vehicles:
            suma += vehicle.get_cars()
        print(f"suma ilosci wagonow to {suma} ")


class DepotBus(Depot):
    def __init__(self, name):
        super().__init__(name)

    def get_description(self):
        super().get_description()
        print("typ to autobusowa")
        suma = 0
        for vehicle in self.list_vehicles:
            suma += vehicle.get_used_fuel()
        print(f"suma ilosci zuzytego paliwa to {suma} ")


depot_tram = DepotTram("zajezdnia tramwajowa")
depot_tram.get_description()
print()
depot_bus = DepotBus("zajezdnia autobusowa")
depot_bus.get_description()
print()
tramwaj1 = Tram(100, 1, depot_tram, 2)
tramwaj2 = Tram(110, 2, depot_tram, 4)
tramwaj1.get_description()
tramwaj2.get_description()
autobus1 = Bus(120, 3, depot_bus, 400)
autobus2 = Bus(130, 4, depot_bus, 500)
print()
depot_tram.get_description()
depot_bus.get_description()
print()
