# Napisz funkcję, która jako argument przyjmuje 10-cio elementową listę liczb całkowitych.
# Ma ona zwrócić przefilitrowaną listę elementów składającą się tylko z liczb dwucyfrowych
# wyselekecjonowanych z odebranej listy.

list_ = [1, 44, 66, 123]


def zad6(arg_list: list):
    list_in = []
    for arg in arg_list:
        if 10 <= arg < 100:
            list_in.append(arg)
    return list_in


print(zad6(list_))
