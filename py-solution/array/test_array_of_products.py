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


def brute_force_solution(array):
    """
      Time: O(n^2)
      Space: O(n)
    """
    products = [1 for _ in range(len(array))]
    for i in range(len(array)):
        running_product = 1
        for j in range(len(array)):
            if i != j:
                running_product *= array[j]
        products[i] = running_product
    return products


def array_of_products_clean(array):
    """
      Time: O(n)
      Space: O(n)
    """
    products = [1 for _ in range(len(array))]

    left_running_product = 1
    for i in range(len(array)):
        products[i] = left_running_product
        left_running_product *= array[i]

    right_running_product = 1
    for i in reversed(range(len(array))):
        products[i] *= right_running_product
        right_running_product *= array[i]

    return products


def array_of_products(array):
    """
      Time: O(n)
      Space: O(n)
    """
    products = [1 for _ in range(len(array))]
    left_products = [1 for _ in range(len(array))]
    right_products = [1 for _ in range(len(array))]

    left_running_product = 1
    for i in range(len(array)):
        left_products[i] = left_running_product
        left_running_product *= array[i]

    right_running_product = 1
    for i in reversed(range(len(array))):
        right_products[i] = right_running_product
        right_running_product *= array[i]

    for i in range(len(array)):
        products[i] = left_products[i] * right_products[i]

    return products


def test_array_of_products():
    array = [5, 1, 4, 2]
    output = [8, 40, 10, 20]
    assert array_of_products(array) == output
    assert brute_force_solution(array) == output
    assert array_of_products_clean(array) == output
    assert array_of_products_non_opt_solution(array) == output
