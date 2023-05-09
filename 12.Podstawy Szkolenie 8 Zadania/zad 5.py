with open("przyklad.txt", encoding="utf-8") as plik:
   plik.tell()
   plik.seek(43)
   print(plik.read(1)) # ???