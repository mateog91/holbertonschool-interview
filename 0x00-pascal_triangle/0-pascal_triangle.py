#!/usr/bin/python3
"""
Module for pascal triangle function
"""
def pascal_triangle(n):
    #initial result
    result = [[1]]

    #outer loop for rows
    for i in range(n - 1):
        #create temporary row
        temp_row = [0] + result[-1] + [0]
        # calculate length of new row
        new_row_length = len(result[-1]) + 1
        # new_row = []
        # for j in range(new_row_length):
        #     new_row.append(temp_row[j] + temp_row[j + 1])

        new_row = [temp_row[j] + temp_row[j + 1] for j in range(new_row_length)]

        result.append(new_row)
    return result