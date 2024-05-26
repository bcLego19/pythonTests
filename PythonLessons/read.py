with open("cheese.txt", "r") as file:
    file_text = file.read()
    print(file_text)

with open("cheese.txt", "r") as file:
    lines = file.readlines()
    print(lines)

with open("cheese.txt", "r") as file:
    for line in file:
        print(line)

with open("numbers.txt", "r") as file:
    total = 1
    for line in file:
        try:
            number = float(line)
            total *= number
        except Exception as e:
            pass

    print(total)