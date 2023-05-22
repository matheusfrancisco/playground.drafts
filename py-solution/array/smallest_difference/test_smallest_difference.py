

# O(nlog(n) + mlog(m)) time
# O(1) space
def smallest_difference(array_one, array_two):
    array_one.sort()
    array_two.sort()
    array_one_index = 0
    array_two_index = 0
    smallest_pair = []
    smallest = float('inf')
    current = float('inf')
    while(
        array_one_index < len(array_one) and array_two_index < len(array_two)
    ):
        first_num = array_one[array_one_index]
        second_num = array_two[array_two_index]
        if first_num < second_num:
            current = second_num - first_num
            array_one_index += 1
        elif second_num < first_num:
            current = first_num - second_num
            array_two_index += 1
        else:
            return [first_num, second_num]
        if smallest > current:
            smallest = current
            smallest_pair = [first_num, second_num]
    return smallest_pair


def test_smallest():
    assert [28, 26] == smallest_difference(
        [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]
    )
