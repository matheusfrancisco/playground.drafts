

"""
Problem: Climbing Stairs k steps

you are climbing a stair case. It takes n steps
to reach to the top. Each time you can either climb 1
, 2  or 3 steps. In how many distinct ways can you climb to the
top?
but we are not allowed to setp on red stairs

"""

def climbstairskred(n: int, k: int, stairs: list[bool]) -> int:
    """
        time complexity O(nk)
        space O(k)
        stairs = [flase, true, flase, false, true, false]
    """
    dp = [0] * k
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(1, k):
            if i - j < 0:
                continue
            if stairs[i-1]:
                dp[i % k] = 0
            else:
                dp[i % k] += dp[(i-j) % k]

    return dp[n % k]


assert climbstairskred(7, 3, [False, True, False, True, True, False, False, ]) == 2
