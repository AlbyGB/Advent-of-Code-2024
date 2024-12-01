import re

f_list = []
s_list = []

regex = r'\b\d+\b'

somma = 0

with open('inputs/problem1input.txt', 'r') as file:
    for riga in file:
        numeri = list(map(int, re.findall(regex, riga)))
        f_list.append(numeri[0])
        s_list.append(numeri[1])

    f_list.sort()
    s_list.sort()

    for i, el in enumerate(f_list):
        somma += abs((el - s_list[i]))


print(somma)
