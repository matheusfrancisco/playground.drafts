
"""
Problem Statement#
Any number will be called a happy number if, after repeatedly replacing it 
with a number equal to the sum of the square of all of its digits, leads us to 
number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they 
will be stuck in a cycle of numbers which does not include ‘1’.
time complexity: O(n)
"""


def find_happy_number(num):
    slow, fast = num, num
    while True:
        slow = find_square(slow)
        fast = find_square(find_square(fast))
        if slow == fast:
            break
    return slow == 1


def find_square(num):
    _sum = 0
    while num > 0:
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum

def is_happy_number(n):
    slow, fast = n, sum_digits(n)
    while slow != fast:
        slow = sum_digits(slow)
        fast = sum_digits(sum_digits(fast))

    if slow == 1 or fast == 1:
        return True

    return False

def sum_digits(number):  # Helper function that calculates the sum of digits.
    total_sum = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        total_sum += digit ** 2
    return total_sum

def main():
    print(find_happy_number(23))
    print(find_happy_number(12))

    print(is_happy_number(19))


main()
