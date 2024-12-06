file_path = "day5/input.txt"
result = 0

order = []

inputs = []

with open(file_path, "r") as file:
    content = file.read()
    splitted_content = content.split("\n")
    rules = True
    for line in splitted_content:
        if line == "":
            rules = False
            continue
        if rules:
            splitted_rule = line.split("|")
            n1 = int(splitted_rule[0])
            n2 = int(splitted_rule[1])
            order.append((n1, n2))
        else:
            splitted_line = line.split(",")
            numbers = []
            for num in splitted_line:
                numbers.append(int(num))
            inputs.append(numbers)
            
    for input in inputs:
        valid = True
        for i, number in enumerate(input):
            for j in range(i + 1, len(input)):
                if (number, input[j]) not in order:
                    valid = False
        if valid:
            result += input[len(input) // 2]
            
    print(result)