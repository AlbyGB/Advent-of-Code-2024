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
        report_is_valid = False
        for i in range(0, len(report)):
            new_report = report.copy()
            new_report.pop(i)
            order = 0
            if new_report[0] < new_report[1]:
                order = 1 # ascending
            else:
                order = 0 # descending
            valid = True  
            for i in range(0, len(new_report) - 1): 
                if order == 1:
                    if new_report[i] >= new_report[i + 1] or (int(new_report[i + 1]) - int(new_report[i])) > 3:
                        valid = False
                        break
                else:
                    if new_report[i] <= new_report[i + 1] or (int(new_report[i]) - int(new_report[i + 1])) > 3:
                        valid = False
            if valid:
                report_is_valid = True
                break
        
        if report_is_valid:
            result += 1
    
        
    print(result)