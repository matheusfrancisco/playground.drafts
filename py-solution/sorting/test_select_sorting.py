def selection_sort(array):
    """
      Time O(n^2)
      Space O(1)
      Write a function that takes in an array of integers and returns
      a sorted version of that array. Use the selection sort algorithm
      to sort the array.
    """
    current_idx = 0
    while current_idx < len(array) - 1:
        smallest_idx = current_idx
        for i in range(current_idx + 1, len(array)):
            if array[smallest_idx] > array[i]:
                smallest_idx = i
        swap(current_idx, smallest_idx, array)
        current_idx += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def test_selection_sort():
    array = [8, 5, 2, 9, 6, 3, 5]
    sorted_array = [2, 3, 5, 5, 6, 8, 9]
    assert selection_sort(array) == sorted_array
