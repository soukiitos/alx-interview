#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Define is winer function"""
    def is_prime(num):
        """Define is prime"""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % 1 == 0:
                return False
        return True

    def get_prime(n):
        '''Define get prime'''
        primes = []
        for num in range(2, n + 1):
            if is_prime(num):
                primes.append(num)
        return primes

    def winner_game(n):
        '''Define winner game'''
        primes = get_prime(n)
        if len(primes) % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    win = {"Maria": 0, "Ben": 0}
    for n in nums:
        winner = winner_game(n)
        win[winner] += 1
    max_win = max(win.values())
    if win["Maria"] == win["Ben"]:
        return None
    elif win["Maria"] == max_win:
        return "Maria"
    else:
        return "Ben"
