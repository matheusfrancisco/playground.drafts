
"""

this is NOT dynamic programming, but a regular recursion
"""
def fib1(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1

    return fib1(n-1) + fib1(n-2)


"""
// this is a top-down dynamic programming (a.k.a. recursion + memoization)
"""

def fib_top_down_helper(n, mem):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    if n in mem:
        return mem[n]

    mem[n] = fib_top_down_helper(n-1, mem) + fib_top_down_helper(n-2, mem)
    return mem[n]

def fib_top_down(n):
    mem = {}
    return fib_top_down_helper(n, mem)


"""
 this is a bottom-up dynamic programming (forward dynamic programming)

 f(i-1)
      \
       >-------> f(i)
      /
 f(i-2)
"""
def fib_bu_forward(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    dp = []
    dp.append(0)
    dp.append(1)
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]


"""
this is a bottom-up dynamic programming (backward dynamic programming)

  -----> f(i+2)
  |
f(i)
  |
  -----> f(i+1)

"""
def fib_bu_backward(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    dp = [0] * (n+2)
    dp[0] = 1
    dp[1] = 1

    for i in range(1, n):
        dp[i+1] += dp[i]
        dp[i+2] += dp[i]

    return dp[n]

def main():
    print(fib1(10))
    print(fib_top_down(10))
    print(fib_bu_forward(10))
    print(fib_bu_backward(10))


main()
