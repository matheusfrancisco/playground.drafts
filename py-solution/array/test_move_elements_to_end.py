"""
You're given an array of integers and an integer. Write a function that moves all
instances of that integer in the array to the end of the array and return the array

The func should perform this in place(i.e it should mutate the input array)
and doesn't need to maintain the order of the other integers

"""


def test_move_to_the_end():
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    to_move = 2
    array_moved = [4, 1, 3, 2, 2, 2, 2, 2]
    assert move_element_to_end(array, to_move) == array_moved
    assert move_element_to_end2(array, to_move) == array_moved


def move_element_to_end(array, to_move):
    """
      O(n) time
      O(1) space
    """
    j = len(array) - 1
    i = 0
    while i < j:
        print(i)
        print(j)
        current = array[i]
        swapped = array[j]
        if current == to_move and swapped == to_move:
            j -= 1
        elif current == to_move and swapped != to_move:
            swap(array, i, j)
            i += 1
            j -= 1
        elif current != to_move and swapped != to_move:
            i += 1
        elif current != to_move and swapped == to_move:
            j -= 1
    return array


def move_element_to_end2(array, to_move):
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == to_move:
            j -= 1
        if array[i] == to_move:
            swap(array, i, j)
        i += 1
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
