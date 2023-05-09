SLOWNIK = {'The Sensual World': 'Kate Bush', 'Shaday': 'Ofra Haza', 'Achtung Baby': 'U2',
           'Aion': 'Dead Can Dance', 'Invisible Touch': 'Genesis'}
print(SLOWNIK)
klucz1 = 'The Sensual World'
klucz2 = "lalka"

print(SLOWNIK.keys())

if klucz1 in SLOWNIK.keys():
    print("Wykonawcą albumu " + klucz1 + " jest  " + SLOWNIK[klucz1])
    print(f"Wykonawcą albumu {klucz1} jest {SLOWNIK[klucz1]}")