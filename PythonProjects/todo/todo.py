import sys
FILENAME = "todo_data.txt"

# Read File

# Add Todo

# Remove Todo

# Save File

# Print List
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