
def insert_sort(array):
    """
       write a function that takes in an
       array of int and returns a sorted version of that array.
       Use the insert sort algorithm to sort the array.

       Space O(1)
       Time O(n^2)
    """
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j -= 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def test_insert_sort():
    assert [2, 3, 5, 5, 6, 8, 9] == insert_sort([8, 5, 2, 9, 5, 6, 3])
