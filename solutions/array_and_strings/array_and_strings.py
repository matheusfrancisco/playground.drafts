from collections import Counter


def is_unique_with_counter(string):
    """
      Time complexity:
        Best case: O(n)
        Worst case: O(n)

    """
    letters = Counter(string)
    for count in letters.values():
        if count > 1:
            return False
    return True


def is_unique(string):
    """
      Time complexity:
        Best case: O(n)
        Worst case: O(n)

    """
    letters = {}
    for letter in string:
        if letter in letters:
            return False
        letters[letter] = True
    return True
