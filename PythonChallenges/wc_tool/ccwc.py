"""
Code your own word count program:
Implements wc, which is a function for word, line, character, and byte count
See man wc in your local terminal for more
"""

import sys

LEGAL_COMMANDS = ["-c", "-l", "-w", "-m"]

def legal_commands(input, legal_input):
    return input in legal_input

def read_data(source):
    if source == "-": # check for standard input flag
        # read from standard input
        return sys.stdin.read()
    else:
        try:
            with open(source, "rb") as file:
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

def defaultAction(data, filename):
    if data:
        byteCount = countBytes(filename)
        lineCount = countLines(data)
        wordCount = countWords(data)
    print(f"    {lineCount} {wordCount} {byteCount} {filename}")
    return [lineCount, wordCount, byteCount]

def main():
    if (len(sys.argv) == 1):
        print(f"ccwc {LEGAL_COMMANDS} \"test.txt\"")
    elif (len(sys.argv) == 2 and legal_commands(sys.argv[1], LEGAL_COMMANDS)):
        command = sys.argv[1]
        data = read_data("-")  # Read from standard input
        if data:
            if (command == "-c"):
                byteCount = countBytes(data)
                print(str(byteCount))
            elif (command == "-l"):
                lineCount = countLines(data)
                print(str(lineCount))
            elif (command == "-w"):
                wordCount = countWords(data)
                print(str(wordCount))
            elif (command == "-m"):
                charCount = countChars(data)
                print(str(charCount))
    elif (len(sys.argv) >= 2 and not legal_commands(sys.argv[1], LEGAL_COMMANDS)):
        totalBytes = 0
        totalLines = 0
        totalWords = 0
        temp = []
        for filename in sys.argv[1:]:
            data = read_data(filename)
            if data:
                temp = defaultAction(data, filename)
                totalLines += temp[0]
                totalWords += temp[1]
                totalBytes += temp[2]
        print(f"    {totalLines}    {totalWords}    {totalBytes} total")

    else:
        command = sys.argv[1]
        totalBytes = 0
        totalLines = 0
        totalWords = 0
        totalChars = 0
        for filename in sys.argv[2:]:
            data = read_data(filename)
            if (command == "-c"):
                byteCount = countBytes(sys.argv[2])
                print(f"    {byteCount} {filename}")
                totalBytes += byteCount
            elif (command == "-l"):
                lineCount = countLines(data)
                print(f"    {lineCount} {filename}")
                totalLines += lineCount
            elif (command == "-w"):
                wordCount = countWords(data)
                print(f"    {wordCount} {filename}")
                totalWords += wordCount
            elif (command == "-m"):
                charCount = countChars(data)
                print(f"    {charCount}   {filename}")
                totalChars += charCount
        
        if(totalBytes != 0):
            print(f"    {totalBytes}    total")
        elif(totalLines != 0):
            print(f"    {totalLines}    total")
        elif(totalWords != 0):
            print(f"    {totalWords}    total")
        elif(totalChars != 0):
            print(f"    {totalChars}    total")
        else:
            print("Error counting totals :\\")

main()