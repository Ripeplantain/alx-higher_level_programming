#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieve an element in a list"""
    return(my_list[idx] if 0 <= idx < len(my_list) else "None")
