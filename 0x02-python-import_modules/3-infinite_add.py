#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    suma = 0
    for i in range(1, length):
        suma += int(argv[i])
    print("{}".format(suma))
