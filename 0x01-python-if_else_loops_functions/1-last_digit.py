#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
        laas_digit = number % 10
    else:
        laas_digit = number % -10

        print("Last digit of {} is {}".format(number, laas_digit), end='')

        if laas_digit > 5:
            print(" and is greater than 5")
        elif laas_digit == 0:
            print(" and is 0")
        else:
            print(" and is less than 6 and not 0")
