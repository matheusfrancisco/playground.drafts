
def find_three_largest_numbers(array):
    """
      Time: O(n)
      Complexity O(1)

    """
    three_largest = [None, None, None]
    for num in array:
        update_largest(three_largest, num)
    return three_largest


def update_largest(three_largest, num):
    if three_largest[2] is None or num > three_largest[2]:
        shif_and_update(three_largest, num, 2)
    elif three_largest[1] is None or num > three_largest[1]:
        shif_and_update(three_largest, num, 1)
    elif three_largest[0] is None or num > three_largest[0]:
        shif_and_update(three_largest, num, 0)


def shif_and_update(array, num, idx):
    """
    [0, 1, 2]
    [y, z, num]
    for i in range(0, 2 + 1)
      if i == 2
        ar[2] = num
      else:
        ar[i] = ar[i+1]
    """
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]
    return array


def test_find_three_largest_numbers():
    arr = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    assert find_three_largest_numbers(arr) == [18, 141, 541]
