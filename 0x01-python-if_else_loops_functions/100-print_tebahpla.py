#!/usr/bin/python3
for n in range(122, 96, -1):
    if n % 2 == 0:
        c = chr(n)
        print("{}".format(c), end='')
    else:
        c = chr(n - 32)
        print("{}".format(c), end='')
