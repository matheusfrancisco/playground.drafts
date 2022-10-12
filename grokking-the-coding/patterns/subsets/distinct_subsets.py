
""" Problem Statement

Given a set with distinct elements, find all of its distinct subsets.

Example 1:

Input: [1, 3]
Output: [], [1], [3], [1,3]

Example 2:

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
"""


def find_subsets(nums):
    """doc
        time complexity O(2^n)
        Since, in each step, the number of subsets doubles as we add each element to all
        the existing subsets, therefore, we will have a total of O(2^N)
        subsets, where ‘N’ is the total number of elements in the input set.
        And since we construct a new subset from an existing set, therefore, the time complexity of the above algorithm will be O(N*2^N)

        Space complexity#
        All the additional space used by our algorithm is for the output list. Since we will have a total of O(2^N)
        subsets, and each subset can take up to O(N)
        space, therefore, the space complexity of our algorithm will be O(N*2^N)
    """
    subsets = [[]]

    idx = 0
    while idx < len(nums):
        n = nums[idx]
        set_size = len(subsets)
        j = 0
        while j < set_size:
            s = subsets[j]
            n_subset = s.copy()
            n_subset.append(n)
            subsets.append(n_subset)
            j += 1

        idx += 1

    return subsets

def find_subsets_approach_2(nums):
    subsets = []
    subsets.append([])
    for curr in nums:
        n = len(subsets)
        for i in range(n):
            set1 = list(subsets[i])
            set1.append(curr)
            subsets.append(set1)

    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))
    print("Here is the list of subsets: " + str(find_subsets_approach_2([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets_approach_2([1, 5, 3])))


main()
