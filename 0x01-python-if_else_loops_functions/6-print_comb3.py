#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i < j:
            print("{:d}{:d}".format(i, j), end='')
            if i in [8] and j in [9]:
                continue
            else:
                print(', ', end='')
print('')
