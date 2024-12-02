
file_path = "day1/input.txt"
result = 0
left_list = []
right_list = []

with open(file_path, "r") as file:
    content = file.read()
    splitted_content = content.split("\n")
    for i in splitted_content:
        single_numbers = i.split(" ")
        left_list.append(single_numbers[0])
        right_list.append(single_numbers[3])
  
    for number in left_list:
        occourance = right_list.count(number)
        result += occourance * int(number)
            
    print(result)