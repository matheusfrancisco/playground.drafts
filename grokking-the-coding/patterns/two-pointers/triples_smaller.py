

def triplet_with_smaller_sum(arr, t):
    arr.sort()
    count = 0
    for i in range(len(arr)-2):
        count += search_pair(arr, t - arr[i], i)

    return count


def search_pair(arr, target_sum, first):
    count = 0
    left, right = first + 1, len(arr) - 1

    while(left < right):
        if arr[left] + arr[right] < target_sum:
            count += right - left
            left += 1
        else:
            right -= 1
    return count


def main():
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()
