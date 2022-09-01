#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    temporary = []
    for x in matrix:
        temporary.append(list(map(lambda x: x**2,x)))
    return temporary