def remove_element(arr, key):
    non = 0;
    i = 0
    while i < len(arr) - 1:
        if arr[i] != key:
            arr[non] = arr[i]
            non += 1
        i += 1
    return non


def main():
  print("Array new length: " +
        str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
  print("Array new length: " +
        str(remove_element([2, 11, 2, 2, 1], 2)))


main()


    
