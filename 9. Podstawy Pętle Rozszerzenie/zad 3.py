PEOPLE = ['Adam', 'Stanisław', 'Joanna', 'Kornelia', 'Kacper']

for i in range(len(PEOPLE)):
    for j in range(len(PEOPLE)):
        if j > i:
            print(f"polaczenie {PEOPLE[i]}  z  {PEOPLE[i]}")
