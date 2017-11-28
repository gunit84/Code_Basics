#!python3

"""Python 3 Command Line Arguments with Argparse... """

__author__ = "Gavin Jones"

import argparse

# Entry Point for the Program
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help="first number")
    parser.add_argument("--number2", help="second number")
    # Tells in the -h option only the list of valid operations...
    parser.add_argument("--operation", help="operation", choices=["add", "subtract", "multiply"])
    args = parser.parse_args()

    # Print the Positional Arguments out.
    print(args.number1)
    print(args.number2)
    print(args.operation)

    # Turn the Strings into Integers so they can be used in Operations
    n1 = int(args.number1)
    n2 = int(args.number2)

    # Code logic from the Operation
    if args.operation == "add":
        print("Result:", n1 + n2)
    elif args.operation == "minus":
        print("Result:", n1 - n2)
    elif args.operation == "multiply":
        print("Result:", n1 * n2)
    elif args.operation == "divide":
        print("Result:", n1 / n2)
    else:
        print("Unsupported Operation")
