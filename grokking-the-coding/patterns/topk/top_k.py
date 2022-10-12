
"""
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Note: For a detailed discussion about different approaches to solve this problem, 
take a look at Kth Smallest Number.

Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]
Example 2:

Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]


Solution#
A brute force solution could be to sort the array and return the largest K numbers.
The time complexity of such an algorithm will be O(N*logN)
 
as we need to use a sorting algorithm like Timsort if we use Java’s Collection.sort(). 
Can we do better than that?

Best ds is an HEAP
"""
