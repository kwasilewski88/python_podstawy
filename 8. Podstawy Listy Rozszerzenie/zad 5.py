ZDANIE = "Ala . ma kota ?"

LIST_CHARS = ",.:;,!?"

checks = ["i", 'w', 'na', 'pod', 'dla']

for char in LIST_CHARS:
    ZDANIE = ZDANIE.replace(char, " ")

print(ZDANIE)
zdanie = ZDANIE.split()
print(len(zdanie))

ile = 0
for slowo in zdanie:
    if slowo[0].capitalize() == slowo[0]:
        print(slowo)
        ile += 1
if ile == 0:
    print("Nie ma takich wyrazow", ile)

czy = 0
for check in checks:
    for i in range(len(zdanie)):
        if zdanie[i] == check:
            print("jest to wyraz ", zdanie[i], " o indeksie ", i)
            czy += 1
if czy == 0:
    print('ni ma')
