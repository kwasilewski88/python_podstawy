n = 10
A = set()
B = set()
for i in range(n):
    if i % 2 == 0:
        A.add(i)
    if i % 3 == 2:
        B.add(i)
print(A)
print(B)


print(A | B)
print(A & B)
print(A - B)
print(B ^ A)
