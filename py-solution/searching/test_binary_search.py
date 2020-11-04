def binary_search(array, target):
    """
      Time O(log(n)) => n is len of array
      Space O(log(n))

      Write a func that takes in a sorted array of
      integers as well as a target integer. The
      function should use the binary search
      algorithm to determine if the target integer
      is contained in the arrau and should return its
      index if it is, otherwise -1

    """
    return binary_search_helper(array, target, 0, len(array) - 1)


def binary_search_helper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    match = array[middle]
    if target == match:
        return middle
    elif target < match:
        return binary_search_helper(array, target, left, middle - 1)
    else:
        return binary_search_helper(array, target, middle + 1, right)


def test_binary_search():
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    assert binary_search(array, 33) == 3


def binary_search_it(array, target):
    """
      Time O(log(n)) => n is len of array
      Space O(1)

      Write a func that takes in a sorted array of
      integers as well as a target integer. The
      function should use the binary search
      algorithm to determine if the target integer
      is contained in the arrau and should return its
      index if it is, otherwise -1

    """
    return binary_search_helper_it(array, target, 0, len(array) - 1)


def binary_search_helper_it(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        match = array[middle]
        if target == match:
            return middle
        elif target < match:
            right = middle - 1
        else:
            left = middle + 1
    return - 1


def test_binary_search_iterative():
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    assert binary_search_it(array, 33) == 3
