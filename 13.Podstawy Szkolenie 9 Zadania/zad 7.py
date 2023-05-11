# Utworzyć klasy Notatka (Note) i Notatnik (Notebook).
# Klas notatki przechowuje autora, treść i czas utworzenia (autor i treść są podawane jako argumenty konstruktora,
# a czas jest pobierany i zapisywany przy tworzeniu obiektu).
# Konstruktor klasy Notatnik nie przyjmuje żadnych argumentów,
# lecz tworzy pustą listę do której będą dodawane obiekty klasy Notatka.
# Klasa Notatnika musi posiadać implementacje metod, pozwalających:
# dodać nową notatkę,
# dodać istniejącą notatkę,
# sprawdzić ile jest dodanych notatek,
# wyświetlić wszystkie dodane notatki.
# Dodatkowo musi być obsłużona sytuacja kiedy notatnik jest pusty.
#
# Przykład:
# >>> nb = Notebook()
# >>> nb.dodaj_nowa("Bartek", "Dokonczyc instrukcje")
# >>> nb.wyswietl_wszystko()
# Masz takie notatki:
# 1. Bartek: "Dokonczyc instrukcje" o godzinie 22:18
# >>> n1 = Note("Andrii", "Sprawdzic instrukcje ")
# >>> nb.dodaj(n1)
# >>> nb.wyswietl_wszystko()
# Masz takie notatki:
# 1. Bartek: "Dokonczyc instrukcje" o godzinie 22:18
# 2. Andrii: "Sprawdzic instrukcje" o godzinie 22:20

from datetime import datetime


class Note:
    def __init__(self, author, contents):
        self.author = author
        self.contents = contents
        self.created_time = datetime.now()


class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def add_new_note(self, author, contents):
        note = Note(author, contents)
        self.notes.append(note)

    def get_count_notes(self):
        return self.notes.count

    def show_all_notes(self):
        if not self.notes:
            print()
            print("Notebook is empty")
        else:
            for note in self.notes:
                print()
                print(note.author , note.contents , note.created_time)

nb = Notebook()
nb.add_new_note("Bartek", "Dokonczyc instrukcje")
nb.show_all_notes()
# Masz takie notatki:
# 1. Bartek: "Dokonczyc instrukcje" o godzinie 22:18
n1 = Note("Andrii", "Sprawdzic instrukcje ")
nb.add_note(n1)
nb.show_all_notes()
# Masz takie notatki:
# 1. Bartek: "Dokonczyc instrukcje" o godzinie 22:18
# 2. Andrii: "Sprawdzic instrukcje" o godzinie 22:20