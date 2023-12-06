#!/usr/bin/python3
"""Pascal's Triangle Module"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the specified number of rows.

    :param n: The number of rows to generate in Pascal's Triangle.
    :type n: int

    :return: A list representing Pascal's Triangle with 'n' rows.
    :rtype: list
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        current_row = triangles[-1]
        new_row = [1]
        for i in range(len(current_row) - 1):
            new_row.append(current_row[i] + current_row[i + 1])
        new_row.append(1)
        triangles.append(new_row)
    return triangles
