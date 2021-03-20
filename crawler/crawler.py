import os
import sys

if __name__ == '__main__':
    try:
        argumentList = sys.argv[2:]
        argumentString = ""
        for argument in argumentList:
            argumentString = argumentString + " " + argument
        os.system(f"python {sys.argv[1]}.py {argumentString}")
    except:
        print("An exception occurred")