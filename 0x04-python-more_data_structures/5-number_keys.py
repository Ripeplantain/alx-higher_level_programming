#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    list_dict = list(a_dictionary.keys())
    for i in list_dict:
        count += 1
    return "Number of keys: {}".format(count)    