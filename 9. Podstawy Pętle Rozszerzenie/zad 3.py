LUDZIE  = ['Adam', 'Stanisław', 'Joanna', 'Kornelia', 'Kacper']

for i in range(len(LUDZIE)):
    for j in range(len(LUDZIE)):
        if j > i:
            print(f"polaczenie {LUDZIE[i]}  z  {LUDZIE[i]}")
