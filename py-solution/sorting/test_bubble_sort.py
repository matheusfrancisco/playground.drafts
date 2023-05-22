

def bubble_sort(array):
    """
       write a function that takes in an array of int and returns a sorted version of that array.
       Use the bubble sort algorithm to sort the array.

       Space O(1)
       Time O(n^2)
    """
    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                is_sorted = False
        counter += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def test_bubble_sort():
    assert [2, 3, 5, 5, 6, 8, 9] == bubble_sort([8, 5, 2, 9, 5, 6, 3])
