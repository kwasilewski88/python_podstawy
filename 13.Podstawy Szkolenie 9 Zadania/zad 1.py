# Stwórz klasę reprezentującą studenta.
# Cechy studenta określaj z poziomu konstruktora.
# Dodaj do klasy metodę wyświetlającą informacje o danym obiekcie.

class Student:
    def __init__(self, wiek, wzrost):
        self.wiek = wiek
        self.wzrost = wzrost

    def get_info(self):
        print(f"wiek to {self.wiek} , wzrost to {self.wzrost} w cm")


student1 = Student(23, 178)
student1.get_info()
