"""
Problem:
Coin change
Given an unlimited supply of coins of given denominations,
find the total number of ways to make a change of size n.

Transition function: f(n) = f(n-d_1) + f(n-d_2) + f(n-d_3) + ... + f(n-d_k),
where d_1, d_2, d_3, ..., d_k are provided coin denomations.
"""


def coin_change(n: int) -> int:
    """
    Time complexity O(N)
    Space O(dk)
    coins = 1, 3, 5, 10
    """
    mem = [0] * (n+1)
    mem[0] = 1

    for i in range(1, n+1):
        if i >= 1:
            mem[i] += mem[i-1]
        if i >= 3:
            mem[i] += mem[i-3]
        if i >= 5:
            mem[i] += mem[i-5]
        if i >= 10:
            mem[i] += mem[i-10]

    return mem[n]


assert coin_change(0) == 1
assert coin_change(2) == 1
assert coin_change(3) == 2
assert coin_change(4) == 3
assert coin_change(5) == 5

def coin_change_coins(n: int, coins: list) -> int:
    """
    Time complexity O(N)
    Space O(dk)
    coins = 1, 3, 5, 10
    """
    mem = [0] * (n+1)
    mem[0] = 1

    for i in range(1, n+1):
        for coin in coins:
            if i-coin >= 0:
                mem[i] += mem[i-coin]

    return mem[n]

assert coin_change_coins(0, [1, 3, 5, 10]) == 1
