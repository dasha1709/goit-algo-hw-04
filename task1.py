def total_salary(path):
    try:
        with open(path, "r") as fh:
            count_employees = 0
            total = 0

            while True:
                line = fh.readline().strip()
                if line != '':
                    line = line.split(",")
                    total += int(line[1])
                    count_employees += 1
                else:
                    break
            average = int(total / count_employees)
            return total, average
    except FileNotFoundError:
        return None, None

total, average = total_salary("employees.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
else:
    print("Не вдалося знайти файл або обробити дані.")