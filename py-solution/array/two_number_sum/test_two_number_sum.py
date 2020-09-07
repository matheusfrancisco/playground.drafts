

def two_number_sum(array, target_sum):
  """
    O(n^2) time complexity
    O(1) space
  """
  for i in range(len(array)):
    for j in range(len(array)-1):
        if array[i] != array[j+1]:
            if array[i] + array[j+1] == target_sum:
                return [array[i], array[j+1]]


def two_sum_number_while_loop(array, target_sum):
    """
      O(nlog(n)0) time complexity
	  O(1) space complexity
    """
    array.sort()
    r = len(array) - 1
    l = 0
    while(r > l):
      left_number = array[l]
      right_number = array[r]
      if left_number+right_number == target_sum:
          return [right_number, left_number]
      elif left_number+right_number > target_sum:
          r = r -1
      else:
          l = l + 1
    return []


def two_number_sum_hash_table(array, target_sum):
    """
      O(n) time complexity
      O(n) space complexity

    """
    hash_values = {}
    for number in array:
      current_value = number
      calc = target_sum - current_value
      sum_number = hash_values.get(calc, False)
      if sum_number:
          return [calc, current_value]
      hash_values[current_value] = True
    return []



def test_two_number_sum():
    pair = two_number_sum([3,5,-4,8,11,-1,6], 10)
    assert pair == [11, -1]


def test_two_number_sum_hash_table():
    pair = two_number_sum_hash_table([3,5,-4,8,11,-1,6], 10)
    assert pair == [11, -1]


def test_two_number_sum_while_loop():
    pair = two_sum_number_while_loop([3,5,-4,8,11,-1,6], 10)
    assert pair == [11, -1]
