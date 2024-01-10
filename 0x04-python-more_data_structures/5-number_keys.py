#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    l_keys = list(a_dictionary.keys())

    for i in l_keys:
        num += 1

    return (num)
