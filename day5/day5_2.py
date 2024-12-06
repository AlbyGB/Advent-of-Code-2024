file_path = "day5/input.txt"
result = 0

order = []

inputs = []

def sort_and_find_value(n):
    occourances = []
    for i, el in enumerate(n):
        occourances.append((el, 0))
        for el2 in n:
            if el != el2:
                if (el, el2) in order:
                    occourances[i] = (el, occourances[i][1] + 1)
                    
    occourances.sort(key=lambda x: x[1], reverse=True)
    return occourances[len(occourances) // 2][0]
    

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

        if not valid:
            result += sort_and_find_value(input)
            
    print(result)