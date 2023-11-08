#!/usr/bin/python3
def square_matrix_simple(input_matrix=[]):
    squared_matrix = []
    for row in input_matrix:
        squared_matrix.append([element**2 for element in row])
    return squared_matrix
