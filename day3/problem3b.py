import re

pattern = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'

second_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

file_input = 'input.txt'
file_output = 'day3/output.txt'

"""with open(file_input, 'r') as f:
    testo = f.read()

matches = re.findall(pattern, testo)

with open(file_output, 'w') as f:
    f.write("\n".join(matches))
"""

mul = True

somma = 0

with open(file_output, 'r') as f:
    for riga in f:
        if mul is True:
            if riga == "don't()\n":
                mul = False
                continue
            elif riga != "do()\n":
                match = re.findall(second_pattern, riga)
                somma += int(match[0][0]) * int(match[0][1])
        elif riga == "do()\n":
            mul = True
            continue

print(somma)
