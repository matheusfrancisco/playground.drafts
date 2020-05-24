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


class MyCounter(dict):
    def __missing__(self, key):
        return 0


def is_string_permutation(string, string2):
    """
      Time complexity:
        Best case: O(n logn)
        Worst case: O(n^2)

    """
    counter = MyCounter()
    for letter in string:
        counter[letter] += 1
    for letter in string2:
        if letter not in counter:
            return False
        counter[letter] -= 1
        if counter[letter] == 0:
            del counter[letter]
    return len(counter) == 0


def escape_spaces_urlfy(string):
    return string.strip().replace(" ", "%20")


def string_compression(string):
    """
      Time complexity:
        Best case: O(n logn)
        Worst case: O(n)

    """
    if len(string) == 0:
        return string
    letters = Counter(string)
    parts = [f"{letter}{count}" for letter, count in letters.items()]
    compressed = "".join(parts)
    return compressed
