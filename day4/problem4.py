import re
import os

file_output = "output.txt"

def v_input(linee):
    with open(file_output, "w") as out:
        for i in range(0, len(linee)):
            for j, el2 in enumerate(linee):
                print(i, j)
                out.write(lines[j][i])
            out.write("T")

pattern = r'XMAS|SAMX'

occ = 0

lines = []

with open("input.txt") as f:
    for riga in f:
        match = re.findall(pattern, riga)
        occ += len(match)
        lines.append(riga)

v_input(lines)

with open("output.txt", "r") as out:
    for riga in out:
        match = re.findall(pattern, riga)
        occ += len(match)

print(occ)