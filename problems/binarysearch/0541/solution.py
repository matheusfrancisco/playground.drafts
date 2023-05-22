"""
Implementation

Initially check whether the number given is odd, even or zero.
If it appears to be zero, then directly no bottle is consumed, thus finally returning 0.
If it is ODD, then we know that after consuming 3 bottles he will get an extra one and 
thus the net bottles consumed are 2 (Eg: 9,7,5,3,1,0), therefore at the end he will get 
n//2 (the absolute value) extra bottles with the given n bottles, thus (n+ (n//2)) bottles.

If bottles are EVEN then he will get ONE LESS then the odd bottle case i.e., ((n//2)-1), 
because at the end he won't get three bottles to get the extra one and thus finally will
be short of one (Eg: 14,12,10,8,6,4,2,0). Therefore finally we will return ((n//2)+n-1) bottles.

Example #1
Input:
n=0
Output:
0

Example #2
Input:
n=17
Output:
25
Explanation: n=17 (odd)
Therefore, (n//2) = (17//2) is "8"
finally o/p is : 17 + 8 = 25

Example #3
Input:
n=44
Output:
65
Explanation: n=44 (even)
Therefore, (n//2) = (44//2) is "22"
finally o/p is : 44 + 22 - 1 = 65

Time Complexity
\mathcal{O}(1)O(1), as we are using just if-else conditions and no loops are used, thus we attain this complexity.

Space Complexity
\mathcal{O}(1)O(1), since no extra space is consumed throughout the execution of the program.
"""

"""

You are given an integer n representing n full beer bottles. Given that you can exchange 
3 empty beer bottles for 1 full beer bottle, return the number of beer bottles you can drink.

Constraints

0 ≤ n < 2 ** 31
"""
class Solution:
    def solve(self, n):
        if n == 0:
            return 0
        return n + (n - 1)//2

