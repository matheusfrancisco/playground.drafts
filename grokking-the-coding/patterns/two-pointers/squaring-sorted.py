

def squares (arr):
    squares = [0 for x in range(len(arr))]
    high_index = len(arr) - 1
    left, right = 0, len(arr) -1
    while (left <= right):
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]
        if left_square > right_square:
            squares[high_index] = left_square
            left += 1
        else:
            squares[high_index] = right_square 
            right -= 1
        high_index -= 1

        
    return squares

assert [0, 1, 4, 4, 9] == squares([-2, -1, 0, 2, 3])
