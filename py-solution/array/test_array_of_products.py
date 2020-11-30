"""
Array of products

Write a function that takes in a non-empty array of integers
and returns an array of the same length, where each element
in the output array is equal to the product of every other number
in the input array

In other words the value output[i] is equal to the products of
every number in the input array other than input[i]


"""


def array_of_products_non_opt_solution(array):
    """
      Time: O(n^2)
      Space: O(n)
    """
    output_array = []
    for idx in range(len(array)):
        value = 1
        left_idx = idx - 1
        print(left_idx)
        while left_idx >= 0:
            value *= array[left_idx]
            left_idx -= 1

        right_idx = idx + 1
        while right_idx < len(array):
            value *= array[right_idx]
            right_idx += 1

        output_array.append(value)
    return output_array


# TODO implement opt solution
def array_of_products(array):
    return array_of_products_non_opt_solution(array)


def test_array_of_products():
    array = [5, 1, 4, 2]
    output = [8, 40, 10, 20]
    assert array_of_products(array) == output
    assert array_of_products_non_opt_solution(array) == output
