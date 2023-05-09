LIST_CHARS = ",.:;!?"
zdanie = "Ala . ma kota ?"


for char in LIST_CHARS:
    zdanie = zdanie.replace(char, " ")

print(zdanie)
zdanie = zdanie.split()
print(zdanie)

zdanie.reverse()
print(zdanie)
