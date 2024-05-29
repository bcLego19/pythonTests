"""
Code your own word count program:
Implements wc, which is a function for word, line, character, and byte count
See man wc in your local terminal for more
"""

LEGAL_COMMANDS = ["-c"]

def legal_commands(input, legal_input):
    return input in legal_input

