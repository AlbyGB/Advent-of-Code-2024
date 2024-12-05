file_path = "input.txt"
result = 0
letters = []

def find_vertical(i, j):
    found = 0
    if i + 3 < len(letters) and letters[i + 1][j] == "M" and letters[i + 2][j] == "A" and letters[i + 3][j] == "S":
        found += 1
    if i - 3 >= 0 and letters[i - 1][j] == "M" and letters[i - 2][j] == "A" and letters[i - 3][j] == "S":
        found += 1

    return found
     
def find_horizontal(i, j):
    found = 0
    if j + 3 < len(letters[0]) and letters[i][j + 1] == "M" and letters[i][j + 2] == "A" and letters[i][j + 3] == "S":
        found += 1
    if j - 3 >= 0 and letters[i][j - 1] == "M" and letters[i][j - 2] == "A" and letters[i][j - 3] == "S":
        found += 1
    return found

def find_diagonal(i, j):
    found = 0
    if i + 3 < len(letters) and j + 3 < len(letters[0]) and letters[i + 1][j + 1] == "M" and letters[i + 2][j + 2] == "A" and letters[i + 3][j + 3] == "S":
        found += 1
    if i - 3 >= 0 and j - 3 >= 0 and letters[i - 1][j - 1] == "M" and letters[i - 2][j - 2] == "A" and letters[i - 3][j - 3] == "S":
        found += 1
    if i + 3 < len(letters) and j - 3 >= 0 and letters[i + 1][j - 1] == "M" and letters[i + 2][j - 2] == "A" and letters[i + 3][j - 3] == "S":
        found += 1
    if i - 3 >= 0 and j + 3 < len(letters[0]) and letters[i - 1][j + 1] == "M" and letters[i - 2][j + 2] == "A" and letters[i - 3][j + 3] == "S":
        found += 1
    return found

with open(file_path, "r") as file:
    content = file.read()
    splitted_content = content.split("\n")
    for row in splitted_content:
        list_row = list(row)
        letters.append(list_row)
    for i, letter in enumerate(letters):
        for j, char in enumerate(letter):
            found = 0
            if char == "X":
                found = find_vertical(i, j) + find_horizontal(i, j) + find_diagonal(i, j)
            if found:
                result += found
                
    print(result)