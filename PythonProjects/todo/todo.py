import sys
FILENAME = "todo_data.txt"
todos = []

# Read File
try:
    with open(FILENAME, "r") as file:
        todos = file.readlines()
except:
    pass

# Add Todo
if(len(sys.argv) >= 3 and sys.argv[1].lower() == "add"):
    todos.append(sys.argv[2] +"\n")

# Remove Todo
if(len(sys.argv) >= 3 and sys.argv[1].lower() == "remove"):
    try:
        index_to_delete = int(sys.argv[2])
        if (index_to_delete > 0):
            index_to_delete -= 1
            del(todos[index_to_delete])
    except Exception as e:
        print(e)
        sys.exit(1)

# Save File
file = open(FILENAME, "w")
file.writelines(todos)
file.close()

# Print List
if len(todos) == 0:
    print("You have no todo items :)")
else:
    with open(FILENAME, "r") as file:
        i = 1
        for line in file:
            print(f"{i}. "+line)
            i += 1

# Print Commands
print("\n=========================================\n")
print(f"To view ToDos:\n{sys.argv[0]}")
print(f"\nTo add a ToDo:\n{sys.argv[0]} add \"Clean Room\"\n")
print(f"To remove or complete ToDo:\n{sys.argv[0]} remove 2\n")