file = open("edit.py", "r")
lines = file.readlines()
file.close()

# Edit
lines = ["Hello\n", "My name is nick!"]

# Write
with open("edit.py", "w"):
    file.writelines(lines)