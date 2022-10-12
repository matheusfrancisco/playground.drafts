
def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        n = arr[i]
        if n == i + 1:
            i += 1
        else:
            j = 0
            k = i
            while j == 0:
                n = arr[k]
                aux = arr[n-1]
                arr[n-1] = n
                print(n, aux)
                if aux == k+1:
                    arr[k] = aux
                    j = 1
                    i += 1
                else:
                    arr[k] = aux

    return arr


def cyclic_sort2(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    return nums


def main():
    print(cyclic_sort2([3, 1, 5, 4, 2]))
    print(cyclic_sort2([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort2([1, 5, 6, 4, 3, 2]))


main()

assert [1, 2, 3, 4, 5] == cyclic_sort([3, 4, 2, 1, 5])
