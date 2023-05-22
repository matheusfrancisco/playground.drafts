"""
  Given an array of distinct positive integers representing coin denomination
  and a single non-negative integer n representing a target amount of money,
  write a function that returns the smallest number of coins needed to make
  change for (to sum up to) that amount using the given foin denominations.
  
"""


def min_number_of_coins_change(n, denoms):
    """
      O(coin*d) time
      O(coin) space
    """
    num_of_coins = [float('inf') for amount in range(n + 1)]
    num_of_coins[0] = 0
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                num_of_coins[amount] = min(num_of_coins[amount], 1 + num_of_coins[amount - denom]) # noqa
    return num_of_coins[n] if num_of_coins[n] != float("inf") else -1


def test_min_number_of_coins():
    assert min_number_of_coins_change(6, [1, 2, 4]) == 2
