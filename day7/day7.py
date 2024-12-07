from itertools import product

file_path = "day7/input.txt"
result = 0
equations = []

def res_equation(res, numbers):        
    operations = list(product("+*", repeat=len(numbers) - 1))
    for operation in operations:
        possible_result = numbers[0]
        for i, op in enumerate(operation):
            if op == "+":
                possible_result += numbers[i + 1]
            if op == "*":
                possible_result *= numbers[i + 1]
        if possible_result == res:
            return res        
    return 0

with open(file_path, "r") as file:
    content = file.read().strip()
    lines = content.split("\n")
    for line in lines:
        values  = line.split(": ")
        res = int(values[0])
        numbers = values[1].split(" ")
        int_numbers = []
        for number in numbers:
            int_numbers.append(int(number))
        equations.append((res, int_numbers))


for equation in equations:
    result += res_equation(equation[0], equation[1])
print(result)