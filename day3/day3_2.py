file_path = "day3/input.txt"
result = 0

with open(file_path, "r") as file:
    state = 1
    content = file.read()
    splitted_content = content.split("\n")
    for row in splitted_content:
        for i, char in enumerate(row):
            
            if char == "d" and row[i + 1] == "o" and row[i + 2] == "(" and row[i + 3] == ")":
                state = 1
            elif char == "d" and row[i + 1] == "o" and row[i + 2] == "n" and row[i + 3] == "'" and row[i + 4] == "t" and row[i + 5] == "(" and row[i + 6] == ")":
                state = 0
            
            if state == 1:
                if char == "m" and row[i + 1] == "u" and row[i + 2] == "l" and row[i + 3] == "(":
                    last_char = i + 4;
                    for j in range(i + 4, i  + 12):
                        if row[j] == ")":
                            last_char = j
                            break
                    new_string = row[i + 4:last_char]
                    numbers = new_string.split(",")
                    if len(numbers) == 2:
                        if len(numbers[0]) > 0 and len(numbers[1]) > 0 and len(numbers[0]) < 4 and len(numbers[1]) < 4:
                            result += int(numbers[0]) * int(numbers[1])
                            print(numbers)
    print(result)