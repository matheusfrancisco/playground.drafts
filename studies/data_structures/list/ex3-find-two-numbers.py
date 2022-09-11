"""
Problem Statement#
In this problem, you have to implement the find_sum(lst,k)
function which will take a number k as input and return two numbers that add up to k.

Input#
A list and a number k

Output#
A list with two integers a and b that add up to k

"""
from typing import List


lst = [1, 21, 3, 14, 5, 60, 7, 6]
k = 81


def solution_with_hash(lst: List, k: int):
    h = {}
    for num in lst:
        if k - num in h:
            return [h[k-num], num]
        h[num] = num
    return []


assert [21, 60] == solution_with_hash(lst, k)


"""
Time Complexity#
Since most optimal comparison-based sorting functions take O(nlogn)

O(nlogn)
, let’s assume that the Python .sort() function takes the same.
Moreover, since binary search takes O(logn)

O(logn)
 time for a finding a single element, therefore a binary search 
 for all n elements will take O(nlogn)

O(nlogn)
 time.”

"""


def binary_search(a: List, item: int):
    first = 0
    last = len(a) - 1
    found = False
    index = -1
    while first <= last and not found:
        mid = (first + last) // 2
        if a[mid] == item:
            index = mid
            found = True
        else:
            if item < a[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found:
        return index
    else:
        return -1


def find_sum(lst, k):
    lst.sort()
    for j in range(len(lst)):
        # find the difference in list through binary search
        # return the only if we find an index
        index = binary_search(lst, k - lst[j])
        if index is not -1 and index is not j:
            return [lst[j], k - lst[j]]


print(find_sum([1, 5, 3], 2))
print(find_sum([1, 2, 3, 4], 5))


def find_sum1(lst, k):
    """
    Time Complexity#
    The linear scan takes O(n)
    O(n)
     and sort takes O(n log n)
    O(nlogn)
    . The time complexity becomes O(n log n) + O(n)
    O(nlogn)+O(n)
     because the sort and the linear scan are done one after the other. The overall
     would be O(n log n)
    O(nlogn)
     in the worst case.
    """
    # sort the list
    lst.sort()
    index1 = 0
    index2 = len(lst) - 1
    result = []
    sum = 0
    # iterate from front and back
    # move accordingly to reach the sum to be equal to k
    # returns false when the two indices meet
    while (index1 != index2):
        sum = lst[index1] + lst[index2]
        if sum < k:
            index1 += 1
        elif sum > k:
            index2 -= 1
        else:
            result.append(lst[index1])
            result.append(lst[index2])
            return result
    return False


print(find_sum([1, 2, 3, 4], 5))
print(find_sum([1, 2, 3, 4], 2))


