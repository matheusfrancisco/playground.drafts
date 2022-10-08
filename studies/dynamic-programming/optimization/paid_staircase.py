"""
paid staircase

you are climbing a paid staircase. It takes n steps to reach to the top and you have
to pay a[i] to step on i-th stair. Each time you can climb 1 or 2 steps.

What is the ceapest amount you have to pay to get to the top of the staircase?

"""

def paid_staircase(n: int, p: list[int]):
    """
    Time complexity: O(n)
    space complexity: O(n)
    """

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = p[1]
    for i in range(2, n + 1):
        dp[i] = min(dp[i-1], dp[i-2]) + p[i]

    return dp[n]


assert paid_staircase(3, [0, 3, 2, 4]) == 6
