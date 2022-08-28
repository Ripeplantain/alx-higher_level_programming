#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns length of a string and the first character"""
    length = len(sentence)
    first_char = sentence[0] if length > 0 else "None"
    tup = length, first_char
    return tup