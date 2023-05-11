# Stwórz klasę reprezentującą pojazd.
# Dodaj do niej pola określające maksymalną prędkość obiektu oraz jego przebieg.
# Dodaj do klasy metodę, która zwiększać będzie wartość pola przebiegu o przesłaną wartość typu float.


class Pojazd:
    def __init__(self, speed_max, mileage):
        self.speed_max = speed_max
        self.mileage = mileage

    def mileage_add(self, distance: float):
        self.mileage += distance

    def get_info(self):
        print(f"predkosc maksymalna to {self.speed_max} w km/h, przebieg to {self.mileage} w km")


pojazd1 = Pojazd(230, 123000)
pojazd1.get_info()
pojazd1.mileage_add(10000)
pojazd1.get_info()
