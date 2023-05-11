# Stwórz klasę reprezentującą Prostokąt.
# Dodaj do niej metody obliczające pole i obwód z przechowywanych pól - szerokości i długości.

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_field(self):
        return self.width * self.length


Rectangle1 = Rectangle(2, 5)
print(Rectangle1.get_field())
