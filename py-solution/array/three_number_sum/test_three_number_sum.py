

def three_number_sum(array, target):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == target:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
    return triplets


def test_three_number_sum():
    assert [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]] == three_number_sum([
      12, 3, 1, 2, -6, 5, -8, 6], 0
    )
