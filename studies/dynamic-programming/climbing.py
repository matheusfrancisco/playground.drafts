
"""
Problem: Climbing Stairs 2step

you are climbing a stair case. It takes n steps
to reach to the top. Each time you can either climb 1
or 2 steps. In how many distinct ways can you climb to the
top?

Framework for solving DP problems:
1. Define the objective function
    f(i) is the number of distinct ways to reach the i-th stair.

2. Identify base cases
    f(0) = 1
    f(1) = 1
3. Write down a recurrence relation for the optimized objective function
    f(n) = f(n-1) + f(n-2)
4. What's the order of execution?
    bottom-up
5. Where to look for the answer?



"""


def climb(n: int) -> int:
    """
    time complexity O(n)
    space complexity O(n)
    """
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


def climb_opt(n: int) -> int:
    """
    time complexity O(n)
    space complexity O(1)
    """
    a = 1
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c


assert climb(4) == 5
assert climb_opt(4) == 5
