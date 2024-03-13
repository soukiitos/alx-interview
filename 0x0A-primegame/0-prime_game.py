#!/usr/bin/python3
"""Prime Game"""


def is_primes(n):
    """Define is primes"""
    prime = []
    wins = [True] * (n + 1)
    for i in range(2, n + 1):
        if (wins[i]):
            prime.append(i)
            for j in range(i, n + 1, i):
                wins[j] = False
    return prime


def isWinner(x, nums):
    """Define is winner"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Ben = Maria = 0
    for i in range(x):
        prime = is_primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Ben > Maria:
        return "Ben"
    elif Maria > Ben:
        return "Maria"
    return None
