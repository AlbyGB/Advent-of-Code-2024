import re

reports = []

regex = r'\b\d+\b'

safe_reports = 0

good_values = [1, 2, 3]
good_negative_values = [-1, -2, -3]

with open('../inputs/probleminput2.txt', 'r') as file:
    for riga in file:
        distances = []
        numeri = list(map(int, re.findall(regex, riga)))

        for idx, el in enumerate(numeri):
            if idx != len(numeri) - 1:
                distances.append((numeri[idx+1] - el))

        print(distances)

        if all(0 < x <= good_values[2] for x in distances) and all(numeri[i] < numeri[i + 1] for i in range(len(numeri) - 1)):
            safe_reports += 1
        elif all(good_negative_values[2] <= x < 0 for x in distances) and all(numeri[i] > numeri[i + 1] for i in range(len(numeri) - 1)):
            safe_reports += 1


print(safe_reports)
