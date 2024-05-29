"""
Code your own word count program:
Implements wc, which is a function for word, line, character, and byte count
See man wc in your local terminal for more
"""

import sys

LEGAL_COMMANDS = ["-c", "-l"]

def legal_commands(input, legal_input):
    return input in legal_input

def read_file(filename):
  try:
    with open(filename, "rb") as file:
      return file.read().decode("utf-8")  # Decode for character processing
  except Exception as e:
    print(f"Error opening file: {e}")
    return None

def countBytes(FILENAME):
    try:
        with open(FILENAME, "rb") as file:
            return len(file.read())
    except Exception as e:
        print(e)

def countLines(data):
  return len(data.splitlines())

def main():
    if (len(sys.argv) == 1):
        print(f"ccwc {LEGAL_COMMANDS} \"test.txt\"")
    elif (len(sys.argv) == 2 and legal_commands(sys.argv[1], LEGAL_COMMANDS)):
        print("Too few arguments: Missing file")
    elif (len(sys.argv) >= 3 and legal_commands(sys.argv[1], LEGAL_COMMANDS)):
        command = sys.argv[1]
        filename = sys.argv[2]
        
        data = read_file(filename)
        if (command == "-c"):
            byteCount = countBytes(sys.argv[2])
            print(str(byteCount) + f" {sys.argv[2]}")
        elif (command == "-l"):
            lineCount = countLines(data)
            print(str(lineCount) + f" {filename}")
    else:
        print("Error in execution.")

main()