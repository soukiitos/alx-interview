#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """Rotate 2D Matrix"""
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            matrix[j].append(matrix[i].pop(0))
    for row in matrix:
        row.reverse()
