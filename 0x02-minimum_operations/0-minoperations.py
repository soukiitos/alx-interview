#!/usr/bin/python3
'''Minimum Operations'''


def minOperations(n):
    '''Define minOperations(n)'''
    if (n <= 1):
        return 0
    OP = 0
    num = 2
    while num * num <= n:
        while n % num == 0:
            n //= num
            OP += num
        num += 1

    if n > 1:
        OP += n
    return OP
