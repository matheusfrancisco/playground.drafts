import pytest


def is_palindrome(string):
    """
      Time: O(n)
      Space: O(1)

    """
    has_same_len = 0
    string_inverted = string[::-1]
    print(string_inverted)
    for i in range(len(string)):
        if string_inverted[i] == string[i]:
            has_same_len += 1
    return has_same_len == len(string)


def is_palindrome_without_loop(string):
    """
      Time: O(n)
      Space: O(n)

    """
    string_inverted = string[::-1]
    return string == string_inverted


def is_palindrome_2(string, i=0):
    """
      Time: O(n)
      Space: O(n)

    """
    j = len(string) - 1 - i
    return True if i>= j else string[i] == string[j] and is_palindrome_2(string, i+1) # noqa


@pytest.mark.parametrize(
    "test_input,expected", [('abc', False), ('ovo', True), ('abcdcba', True)]
)
def test_is_palindrome(test_input, expected):
    assert is_palindrome(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected", [('abc', False), ('ovo', True), ('abcdcba', True)]
)
def test_is_palindrome_2(test_input, expected):
    assert is_palindrome_without_loop(test_input) == expected
