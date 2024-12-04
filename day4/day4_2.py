file_path = "day4/input.txt"
result = 0
letters = []

def find_diagonal(i, j):
    found = 0
    if i - 1 >= 0 and j - 1 >= 0 and i + 1 < len(letters) and j + 1 < len(letters[i]):
        if letters[i - 1][j - 1] == "M" and letters[i - 1][j + 1] == "M" and letters[i + 1][j - 1] == "S" and letters[i + 1][j + 1] == "S":        
            found += 1
        if letters[i - 1][j - 1] == "S" and letters[i - 1][j + 1] == "S" and letters[i + 1][j - 1] == "M" and letters[i + 1][j + 1] == "M":        
            found += 1
        if letters[i - 1][j - 1] == "M" and letters[i - 1][j + 1] == "S" and letters[i + 1][j - 1] == "M" and letters[i + 1][j + 1] == "S":        
            found += 1
        if letters[i - 1][j - 1] == "S" and letters[i - 1][j + 1] == "M" and letters[i + 1][j - 1] == "S" and letters[i + 1][j + 1] == "M":
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
            if char == "A":
                found = find_diagonal(i, j)
            if found:
                result += found
                
    print(result)