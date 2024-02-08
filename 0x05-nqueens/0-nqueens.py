#!/usr/bin/python3
'''N queens'''
from sys import argv


def is_nqueen_safe(cell: list) -> bool:
    '''Define is_nqueen_safe'''
    row = len(cell) - 1
    d = 0
    for i in range(0, row):
        d = cell[i] - cell[row]
        if d < 0:
            d *= -1
        if d == 0 or d == row - i:
            return False
    return True


def solve_nqueens(dim: int, r: int, cell: list, o: list):
    '''Define solve_nqueens'''
    if r == dim:
        print(o)
    else:
        for col in range(0, dim):
            cell.append(col)
            o.append([r, col])
            if (is_nqueen_safe(cell)):
                solve_nqueens(dim, r + 1, cell, o)
            cell.pop()
            o.pop()


if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    N = int(argv[1])
except BaseException:
    print('N must be a number')
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)
else:
    o = []
    cell = 0
    solve_nqueens(int(N), cell, [], o)
