#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    lst_num = number % -10
else:
    lst_num = number % 10

print("Last digit of", '{:d}'.format(number), "is", '{:d}'.format(lst_num),
      end="")
if lst_num > 5:
    print(" and is greater than 5")
elif lst_num == 0:
    print(" and is 0")
elif lst_num < 6:
    print(" and is less than 6 and not 0")
