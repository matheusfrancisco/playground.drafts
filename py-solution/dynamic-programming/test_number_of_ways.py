"""
  Given an array of distinct positive integers representing coin denomination
  and a single non-negative integer n representing a target amount of money,
  write a function that returns the number of ways to make change for that
  target amount using the given coin denominations
"""


def number_of_ways(coin, denoms):
    """
      O(coin*d) time
      O(coin) space
    """
    ways = [0] * (coin + 1)
    ways[0] = 1
    for demon in denoms:
        for amount, way in enumerate(ways):
            if demon <= amount:
                ways[amount] = ways[amount] + ways[amount - demon]
    return ways[coin]


def number_of_ways_better(coin, denoms):
    """
      O(coin*d) time
      O(coin) space
    """
    ways = [0 for amount in range(coin + 1)]
    ways[0] = 1
    for demon in denoms:
        for amount in range(1, coin + 1):
            if demon <= amount:
                ways[amount] += ways[amount - demon]
    return ways[coin]


def test_number_of_ways_to_make_change():
    assert number_of_ways(6, [1, 5]) == 2
    assert number_of_ways_better(6, [1, 5]) == 2
    assert number_of_ways(10, [1, 5, 10, 25]) == 4
    assert number_of_ways_better(10, [1, 5, 10, 25]) == 4
