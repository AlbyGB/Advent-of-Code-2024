import regex

input_file = "input.txt"

input_file = open(input_file, "r")
righe = [line.strip() for line in input_file]
input_file.close()

def xmas():
    occ = 0
    for i, riga in enumerate(righe):
        for j, char in enumerate(riga):
            print(i, j)
            if 0 < i < (len(righe) - 1) and 0 < j < (len(riga) - 1):
                if char == "A" and (((righe[i-1][j-1] == "M" and righe[i+1][j+1] == "S") and (righe[i-1][j+1] == "S" and righe[i+1][j-1] == "M")) or ((righe[i+1][j+1] == "M" and righe[i-1][j-1] == "S") and (righe[i-1][j+1] == "M" and righe[i+1][j-1] == "S")) or ((righe[i+1][j+1] == "M" and righe[i-1][j-1] == "S") and (righe[i+1][j-1] == "M" and righe[i-1][j+1] == "S")) or ((righe[i-1][j-1] == "M" and righe[i-1][j+1] == "M") and (righe[i+1][j-1] == "S" and righe[i+1][j+1] == "S"))):
                    occ += 1
    print(occ)

xmas()