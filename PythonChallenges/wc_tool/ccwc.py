"""
Code your own word count program:
Implements wc, which is a function for word, line, character, and byte count
See man wc in your local terminal for more
"""

import sys

LEGAL_COMMANDS = ["-c", "-l", "-w", "-m"]

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

def countWords(data):
   return len(data.split())

def countChars(data):
   return len(data)

def main():
    if (len(sys.argv) == 1):
        print(f"ccwc {LEGAL_COMMANDS} \"test.txt\"")
    elif (len(sys.argv) >= 2 and not legal_commands(sys.argv[1], LEGAL_COMMANDS)):
        filename = sys.argv[1]
        data = read_file(filename)
        if data:
            byteCount = countBytes(filename)
            lineCount = countLines(data)
            wordCount = countWords(data)
        print(f"{lineCount} {wordCount} {byteCount} {filename}")
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
        elif (command == "-w"):
            wordCount = countWords(data)
            print(str(wordCount) + f" {filename}")
        elif (command == "-m"):
            charCount = countChars(data)
            print(str(charCount) + f" {filename}")
    else:
        print("Error in execution.")

main()