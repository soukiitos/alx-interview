#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """MakeChange"""
    if total <= 0:
        return 0
    min_coin = [float('inf')] * (total + 1)
    min_coin[0] = 0
    for coin in coins:
        for tot_coins in range(coin, total + 1):
            min_coin[tot_coins] = min(
                    min_coin[tot_coins],
                    min_coin[tot_coins - coin] + 1
                    )
    return min_coin[total] if min_coin[total] != float('inf') else -1
