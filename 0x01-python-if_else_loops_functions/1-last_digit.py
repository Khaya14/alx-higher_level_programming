#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    laas_digit = number % -10
else:
    laas_digit = number % 10
    if laas_digit > 5:
        print("Last digit of {:d} is {:d} and is greater than 5"
                .format(number, laas_digit))
    elif laas_digit < 6 and laas_digit != 0:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0"
                .format(number, laas_digit))
    else:
        print("Last digit of {:d} is 0 and is 0".format(number))

