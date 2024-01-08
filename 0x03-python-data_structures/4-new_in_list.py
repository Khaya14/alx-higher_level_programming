#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)

    mod_list = my_list[:]

    if 0 <= idx < length:
        mod_list[idx] = element

    return (mod_list)
