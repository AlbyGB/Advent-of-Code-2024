import regex

input_file = "input.txt"
file_output = "output.txt"
d_file_output = "output2.txt"
l_file_output = "output3.txt"

input_file = open(input_file, "r")
righe = [line.strip() for line in input_file]
input_file.close()

n = len(righe)
m = len(righe[0])

def v_input():
    with open(file_output, "w") as out:
        for i in range(0, len(righe)):
            for j, el2 in enumerate(righe):
                print(i, j)
                out.write(righe[j][i])
            out.write("T")

def d_left_input():
    output = []

    with open(l_file_output, 'w') as file:
        for k in range(n + m - 1):
            for i in range(n):
                j = m - 1 - k + i
                if 0 <= j < m:
                    if righe[i][j] != '':
                        output.append(righe[i][j])
            output.append("t")

        file.write(''.join(output))

def d_right_input():
    output = []

    with open(d_file_output, 'w') as file:
        for k in range(n + m - 1):
            for i in range(n):
                j = k - i
                if 0 <= j < m:
                    if righe[i][j] != '':
                        output.append(righe[i][j])
            output.append("t")

        file.write(''.join(output))

pattern = regex.compile(r'XMAS|SAMX')

occ = 0

for riga in righe:
    match = regex.findall(pattern, riga, overlapped=True)
    occ += len(match)

print(f"primo occ {occ}")

v_input()
d_right_input()
d_left_input()

with open("output.txt", "r") as out:
    for riga in out:
        match = regex.findall(pattern, riga, overlapped=True)
        occ += len(match)
    print(f"secondo occ {occ}")

with open("output2.txt", "r") as out:
    for riga in out:
        match = regex.findall(pattern, riga, overlapped=True)
        occ += len(match)
    print(f"terzo occ {occ}")

with open("output3.txt", "r") as out:
    for riga in out:
        match = regex.findall(pattern, riga, overlapped=True)
        occ += len(match)
    print(f"quarto occ {occ}")

print(occ)