

"""
Problem: Climbing Stairs k steps

you are climbing a stair case. It takes n steps
to reach to the top. Each time you can either climb 1
, 2  or 3 steps. In how many distinct ways can you climb to the
top?

Framework for solving DP problems:
1. Define the objective function
    f(i) is the number of distinct ways to reach the i-th stair.

2. Identify base cases
    f(0) = 1
    f(1) = 1
3. Write down a recurrence relation for the optimized objective function
    f(n) = f(n-1) + f(n-2) + ... + f(n-k)
4. What's the order of execution?
    bottom-up
5. Where to look for the answer?



"""


def climb(n: int, k: int) -> int:
    """
    time complexity O(nk)
    space complexity O(n)
    """
    dp = [0] * k
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(1, k):
            if i - j < 0:
                continue
            dp[i % k] += dp[(i-j) % k]

    return dp[n % k]


assert climb(5, 3) == 13

