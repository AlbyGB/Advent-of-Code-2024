import re

reports = []
regex = r'\b\d+\b'
safe_reports = 0

good_values = [1, 2, 3]
good_negative_values = [-1, -2, -3]

def check_row(distances, numbers):
    valid_distances = all(
        x in good_values or x in good_negative_values for x in distances
    )
    valid_numbers = is_valid(numbers)
    return valid_distances and valid_numbers

def is_valid(numbers):
    return all(x < y for x, y in zip(numbers, numbers[1:])) or all(
        x > y for x, y in zip(numbers, numbers[1:])
    )

def adjust_distances(distances):
    temp = []
    for idx, el in enumerate(distances):
        if idx == 0 and el not in good_values and el not in good_negative_values:
            if len(distances) > 1:
                distances[idx + 1] += el
        elif el not in good_values and el not in good_negative_values and temp:
            temp[-1] += el
        else:
            temp.append(el)
    return temp

with open('../inputs/probleminput2.txt', 'r') as file:
    for riga in file:
        distances = []
        numeri = list(map(int, re.findall(regex, riga)))

        for idx, el in enumerate(numeri):
            if idx != len(numeri) - 1:
                distances.append(numeri[idx + 1] - el)

        print("Distanze iniziali:", distances)

        if check_row(distances, numeri):
            safe_reports += 1
            print("Riga valida direttamente")
            continue

        for idx, el in enumerate(numeri):
            new_numbers = numeri[:idx] + numeri[idx + 1:]
            new_distances = [new_numbers[i + 1] - new_numbers[i] for i in range(len(new_numbers) - 1)]

            if check_row(new_distances, new_numbers):
                safe_reports += 1
                print("Riga valida rimuovendo:", el)
                break

        temp = adjust_distances(distances)
        print("Distanze aggiustate:", temp)

        if check_row(temp, numeri):
            safe_reports += 1
            print("Riga valida dopo aggiustamento")

print("Report sicuri:", safe_reports)
