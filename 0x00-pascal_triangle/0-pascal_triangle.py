#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    tr = [[1]]
    for i in range(1, n):
        j = [1]
        for r in range(1, i):
            j.append(tr[i-1][r-1] + tr[i-1][r])
        j.append(1)
        tr.append(j)
    return tr
