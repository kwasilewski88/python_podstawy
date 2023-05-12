# Stwórz klasę Shape i jej podklasę Square.
# Square ma posiadać konstruktor, który przyjmie length jako argument.
# Obie klasy mają posiadać metodę obliczającą pole figury.
# Domyślnie Shape ma zwracać wartość 0.


class Shape:
    def __init__(self):
        pass

    def get_field(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def get_field(self):
        return self.length ** 2


shape1 = Shape()
print(shape1.get_field())
square = Square(5)
print(square.get_field())
