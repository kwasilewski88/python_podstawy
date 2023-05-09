#
# Poproś użytkownika o podanie 3 dowolnych długości boków trójkąta.
# Sprawdź, czy jest to trójkąt prostokątny (wykorzystaj własność trójkąta prostokątnego,
# która mówi że suma kwadratów dwóch dowolnych boków jest równa kwadratowi długości trzeciego).
#

a = 3
b = 4
c = 5

if (a**2) + (b**2) == (c**2):
    print("jest to trojkąt rownoboczny")
else:
    print("NIE jest to trojkąt rownoboczny")
