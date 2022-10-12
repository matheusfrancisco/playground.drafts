

"""
Problem:
find the sum of the first N numbers.

Objective function:
f(i) is the sum of the first i elements

Recurrence relation:
f(n) = f(n-1) + n
"""

def nsum(n):
    mem = [0] * (n + 1)
    mem[0] = 0
    for i in range(1, n + 1):
        mem[i] = mem[i-1] + i
    return mem[n]


print(nsum(5))
