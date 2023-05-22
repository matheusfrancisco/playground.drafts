"""
Problem:
Coin change
Given an unlimited supply of coins of given denominations,
find the total number of ways to make a change of size n, by
using excatly t coins.
f(i,t) = f(i-1, t-1) + f(i-2, t-1) + f(i-3, t-1) + f(i-5, t-1)
"""
