file = open("modify.txt", "r")
lines = file.readlines()
file.close()

# Edit
lines = ["Hello\n", "My name is nick!"]

# Write
with open("modify.txt", "w"):
    file.writelines(lines)