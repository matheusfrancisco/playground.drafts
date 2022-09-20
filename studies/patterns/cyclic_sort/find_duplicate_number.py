"""
We are given an unsorted array containing ‘n+1’
numbers taken from the range 1 to ‘n’. 
The array has only one duplicate but it can be repeated multiple times.
Find that duplicate number without using any extra space. You are, however,
allowed to modify the input array.


"""


def find_duplicate_nums(nums):

    # TODO can be solve with slow and fast pointer
    i, n = 0, len(nums)
    while i < n:
        if nums[i] != i - 1:
            j = nums[i]
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]
        else:
            i += 1
    return -1


def main():
    print(find_duplicate_nums([1, 4, 4, 3, 2]))
    print(find_duplicate_nums([2, 1, 3, 3, 5, 4]))
    print(find_duplicate_nums([2, 4, 1, 4, 4]))


main()
