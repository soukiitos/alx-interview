#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """MakeChange"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count_coin = 0
    i_coins = 0
    while total > 0:
        if i_coins >= len(coins):
            return -1
        if total - coins[i_coins] >= 0:
            total -= coins[i_coins]
            count_coin += 1
        else:
            i_coins += 1
    return count_coin
