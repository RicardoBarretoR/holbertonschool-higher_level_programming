#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    if op == "+":
        resul = add(a, b)
    elif op == "-":
        resul = sub(a, b)
    elif op == "*":
        resul = mul(a, b)
    elif op == "/":
        resul = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{:d} {} {:d} = {:d}".format(a, op, b, resul))
