file_path = "day2/input.txt"
result = 0
reports = []

with open(file_path, "r") as file:
    content = file.read()
    splitted_content = content.split("\n")
    for i in splitted_content:
        single_numbers = i.split(" ")
        report = []
        for j in single_numbers:
            if j != "":
                report.append(int(j))
        reports.append(report)

    for report in reports:

        order = 0
        if report[0] < report[1]:
           order = 1 # ascending
        else:
            order = 0 # descending
        valid = True  
        for i in range(0, len(report) - 1): 
            if order == 1:
                if report[i] >= report[i + 1] or (int(report[i + 1]) - int(report[i])) > 3:
                    valid = False
                    break
            else:
                if report[i] <= report[i + 1] or (int(report[i]) - int(report[i + 1])) > 3:
                    valid = False
        if valid:
            result += 1
        print(report, valid)
                            
    print(result)