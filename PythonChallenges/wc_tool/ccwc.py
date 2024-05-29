"""
Code your own word count program:
Implements wc, which is a function for word, line, character, and byte count
See man wc in your local terminal for more
"""

import sys

LEGAL_COMMANDS = ["-c"]

def legal_commands(input, legal_input):
    return input in legal_input

def countBytes(FILENAME):
    try:
        count = 0
        with open(FILENAME, "rb") as file:
            for byte in file:
                for c in byte:
                    count += 1
        return count
    except Exception as e:
        print(e)

def main():
    if (len(sys.argv) == 1):
        print(f"ccwc {LEGAL_COMMANDS} \"test.txt\"")
    elif (len(sys.argv) == 2 and legal_commands(sys.argv[1], LEGAL_COMMANDS)):
        print("Too few arguments: Missing file")
    elif (len(sys.argv) >= 3 and legal_commands(sys.argv[1], LEGAL_COMMANDS)):
        command = sys.argv[1]
        #print(command)
        
        if (command == "-c"):
            byteCount = countBytes(sys.argv[2])
            print(str(byteCount) + f" {sys.argv[2]}")
    else:
        print("Error in execution.")

main()