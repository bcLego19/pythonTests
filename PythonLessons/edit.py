file = open("modify.txt", "r")
lines = file.readlines()
file.close()

# Edit
lines = ["Hello\n", "My name is nick!"]

# Write
file = open("modify.txt", "w")
file.writelines(lines)
file.close()

file = open("numbers.txt", "r")
lines = file.readlines()
file.close()
i = 0
for i in range(len(lines)):
    try:
        lines[i] = str(float(lines[i]) * 2) + "\n"
    except Exception as e:
        pass

print(lines)

file = open("numbers.txt", "w")
file.writelines(lines)
file.close()