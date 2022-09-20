
def find_all_duplicates(nums):
    duplicate_numbers = []
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicate_numbers.append(nums[i])

    return duplicate_numbers
