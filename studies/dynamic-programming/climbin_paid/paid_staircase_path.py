
"""
paid staircase

you are climbing a paid staircase. It takes n steps to reach to the top and you have
to pay a[i] to step on i-th stair. Each time you can climb 1 or 2 steps.

What is the ceapest amount you have to pay to get to the top of the staircase?
and return the path (minimum path)

"""

def paid_staircase(n: int, p: list[int]) -> list[int]:
    """
    Time complexity: O(n)
    space complexity: O(n)
    """

    dp = [0] * (n + 1)
    _from = [0] * (len(dp) + 1)
    dp[0] = 0
    dp[1] = p[1]
    for i in range(2, n + 1):
        dp[i] = min(dp[i-1], dp[i-2]) + p[i]
        if dp[i-1] < dp[i-2]:
            _from[i] = (i-1)
        else:
            _from[i] = (i-2)

    path = []
    curr = n

    while curr >= 0:
        path.append(curr)
        curr = _from[curr]
        if curr == 0:
            break

    path.append(0)
    return path[::-1]


assert paid_staircase(8, [0, 3, 2, 4, 6, 1, 1, 5, 8]) == [0, 2, 3, 5, 6, 8]
