#!/usr/bin/python3
def replace_in_list(my_list,idx,element):
    """replaces element at an index in a list"""
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return(my_list)
