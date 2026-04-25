#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_m = []

    for row in matrix:
        squared_row = []

        for value in row:
            squared_row.append(value ** 2)

        squared_m.append(squared_row)
    return squared_m
