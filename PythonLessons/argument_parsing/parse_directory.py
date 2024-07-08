"""
Author:         Conner Batson
Title:          parse directory python file
Description:    Experiment to test how to parse directories passed in as command line arguments
Created:        7/7/2024
Last Edit:      7/7/2024
"""
import sys, os

def main():

    print(len(sys.argv))
    print()

    print(sys.argv)
    print()

    print(sys.argv[1:])
    print()

    argument = None

    if len(sys.argv) == 2:
        argument = sys.argv[1]
    else:
        print("no argument" + "\n")
        return
    
    print(argument + "\n")

    print(os.path.isdir(argument))

    return

main()