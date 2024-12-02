"""
NON FUNZIONANTE
"""

import re

reports = []

regex = r'\b\d+\b'

safe_reports = 0

good_values = [1, 2, 3]
good_negative_values = [-1, -2, -3]

def check_row(dist):
    return (all(0 < x <= good_values[2] for x in dist) and all(
        numeri[i] <= numeri[i + 1] for i in range(len(numeri) - 1))) or (all(
        good_negative_values[2] <= x < 0 for x in dist) and all(
                numeri[i] >= numeri[i + 1] for i in range(len(numeri) - 1)))

def is_valid(numbers):
    return all(x < y for x, y in zip(numbers, numbers[1:])) or all(x > y for x, y in zip(numbers, numbers[1:]))

with (open('../inputs/probleminput2.txt', 'r') as file):
    for riga in file:
        distances = []
        numeri = list(map(int, re.findall(regex, riga)))

        for idx, el in enumerate(numeri):
            if idx != len(numeri) - 1:
                distances.append((numeri[idx + 1] - el))

        print("distances")
        print(distances)

        if check_row(distances):
            if not is_valid(numeri):
                for idx, el in enumerate(numeri):
                    new_numbers = numeri[:idx] + numeri[idx + 1:]
                if is_valid(new_numbers):
                    print("cacca")
                    safe_reports += 1
            else:
                safe_reports += 1
        elif not check_row(distances):
            temp = []

            for idx, el in enumerate(distances):
                if idx == 0 and (el not in good_values and el not in good_negative_values):
                    if len(distances) > 1:
                        distances[idx + 1] += el
                elif (el not in good_values and el not in good_negative_values) and temp:
                    temp[-1] += el
                else:
                    temp.append(el)
            print("temp:")
            print(temp)

            if check_row(temp):
                safe_reports += 1


print(safe_reports)
