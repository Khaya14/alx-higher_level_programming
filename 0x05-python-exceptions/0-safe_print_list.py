#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    sum_total = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
        except:
            break
        else:
            sum_total += 1

    print()
    return(sum_total)
