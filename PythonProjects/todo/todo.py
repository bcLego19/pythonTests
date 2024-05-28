import sys
FILENAME = "todo_data.txt"

def readFile():
    todos = []
    # Read File
    try:
        with open(FILENAME, "r") as file:
            todos = file.readlines()
    except FileNotFoundError:
        print("No existing to-do list found. A new data file will be created.")
    except Exception as e:
        print(f"Error loading list: {e}")
    
    return todos

def addTodo(todos):
    # Add Todo
    if(len(sys.argv) >= 3 and sys.argv[1].lower() == "add"):
        todos.append(sys.argv[2] +"\n")

def removeTodo(todos):
    # Remove Todo
    if(len(sys.argv) >= 3 and sys.argv[1].lower() == "remove"):
        try:
            index_to_delete = int(sys.argv[2])
            if (index_to_delete > 0 and index_to_delete <= len(todos)):
                index_to_delete -= 1
                del(todos[index_to_delete])
            else:
                print(f"Invalid todo index. Please enter a number between 1 and {len(todos)}.")
        except Exception as e:
            print(e)
            sys.exit(1)

def saveFile(todos):
    # Save File
    with open(FILENAME, "w") as file:
        file.writelines(todos)

def printList(todos):
    # Print List
    if len(todos) == 0:
        print("You have no todo items :)")
    else:
        for x in range(len(todos)):
            print(f"{x+1}. {todos[x]}", end="")

def print_usage():
    # Print Commands
    print("\n=========================================\n")
    print(f"To view ToDos:\n{sys.argv[0]}")
    print(f"\nTo add a ToDo:\n{sys.argv[0]} add \"Clean Room\"\n")
    print(f"To remove or complete ToDo:\n{sys.argv[0]} remove 2\n")

def todoMain():
    todos = readFile()
    addTodo(todos)
    removeTodo(todos)
    saveFile(todos)
    printList(todos)
    print_usage()

todoMain()