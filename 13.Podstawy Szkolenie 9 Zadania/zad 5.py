# Stwórz program symulujący talię kart (klasa Deck) oraz pojedyncze karty (klasa Card).
# Karta ma być związana z takimi polami jak: wartość (np. 9) oraz figura (np. Diamond).
# W klasie Deck znajdować ma się lista reprezentująca stos kart w ramach jednej talii.
# W Deck znaleźć mają się takie metody jak:
# shuffle (która może wykorzystywać metodę o tej samej nazwie - shuffle - z biblioteki random)
# oraz deal (która będzie usuwała i zwracała ostatnią kartę z talii).
from random import shuffle


class Deck:
    def __init__(self):
        self.list_values = ["clubs", "diamonds", "hearts", "spades"]
        self.list_figures = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.list_Deck = []
        for value in self.list_values:
            for figure in self.list_figures:
                card = Card(figure, value)
                self.list_Deck.append(card)

    def shuffle(self):
        shuffle(self.list_Deck)

    def deal(self):
        self.list_Deck.pop()

    def get_info(self):
        for card in self.list_Deck:
            print(f"karta {card.get_info()} ")


class Card:
    def __init__(self, figure, value):
        self.figure = figure
        self.value = value

    def get_info(self):
        return self.figure + self.value


Deck1 = Deck()
Deck1.get_info()
print()
Deck1.shuffle()
Deck1.get_info()
print()
Deck1.deal()
Deck1.get_info()
print()
