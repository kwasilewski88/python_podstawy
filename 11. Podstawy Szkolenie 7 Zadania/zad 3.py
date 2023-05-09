# Napisz funkcję fizz_buzz, która przyjmuje argument liczbowy.
# 1. Jeżeli liczba jest podzielna przez 3, funkcja powinna zwrócić “Fizz”.
# 2. Jeżeli liczba jest podzielna przez 5, zwróć “Buzz”.
# 3. Jeżeli liczba jest podzielna równocześnie przez 3 i 5, zwróć “FizzBuzz”.
# 4. W przeciwnym razie, zwracaj przekazaną liczbę.


def fizz_buzz(arg_num):
    if arg_num % 3 == 0 and arg_num % 5 == 0:
        return "FizzBuzz"
    elif arg_num % 3 == 0:
        return "Fizz"
    elif arg_num % 5 == 0:
        return "Buzz"

print(fizz_buzz(3))