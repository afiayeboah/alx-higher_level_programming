#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    args = sys.argv[1:]
    arg_count = len(args)
    valid_operators = ["+", "-", "*", "/"]
    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif args[1] not in valid_operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        num1 = int(args[0])
        num2 = int(args[2])
        operator = args[1]
        if operator == "+":
            print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))
        elif operator == "-":
            print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2)))
        elif operator == "*":
            print("{:d} * {:d} = {:d}".format(num1, num2, mul(num1, num2)))
        elif operator == "/":
            print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))
