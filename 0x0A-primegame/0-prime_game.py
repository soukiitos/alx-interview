#!/usr/bin/python3
"""Prime Game"""

def isWinner(x, nums):
    """Define is winer function"""
    def is_winner_of_game(n):
        """Define the winner of game"""
        if n < 2:
            return "Ben"
        primes = []
        for num in range(2, n + 1):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        if len(primes) % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    win = {"Maria": 0, "Ben": 0}
    for n in nums:
        winner = is_winner_of_game(n)
        win[winner] += 1

    max_win = max(win.values())
    if win["Maria"] == win["Ben"]:
        return None
    elif win["Maria"] == max_win:
        return "Maria"
    else:
        return "Ben"
