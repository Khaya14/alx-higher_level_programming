#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    find_div = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            find_div.append(True)
        else:
            find_div.append(False)

    return (find_div)
