LIST_CHARS = ",.:;!?"

zdanie = "Ala. ma kota ?"


for char in LIST_CHARS:
    zdanie = zdanie.replace(char, " ")

print(len(zdanie.split()))
print(zdanie)
