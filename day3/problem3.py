import re

regex = r'mul\((\d{1,3}),(\d{1,3})\)'

somma = 0

with open('input.txt', 'r') as file:
    for riga in file:
        matches = re.findall(regex, riga)

        for match in matches:
            somma += int(match[0])*int(match[1])

print(somma)