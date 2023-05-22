

def test_logest_palindromic_substring():
    assert longest_palindromic_substring("abaxyzzyxf") == "xyzzyx"


def longest_palindromic_substring(string):
    """
      Write a function that given a string,
      returns its longest palindromic substring
      Complexity Time O(n^2)
      Space O(1)

    """
    current_longest_palindromic = [0, 1]
    for i in range(1, len(string)):
        odd = get_longest_palindrome_from(string, i - 1, i + 1)
        even = get_longest_palindrome_from(string, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        current_longest_palindromic = max(
            longest,
            current_longest_palindromic,
            key=lambda x: x[1] - x[0],
        )
    return string[
        current_longest_palindromic[0]:current_longest_palindromic[1]
    ]


def get_longest_palindrome_from(string, left_idx, right_idx):
    while left_idx >= 0 and right_idx < len(string):
        if string[left_idx] != string[right_idx]:
            break

        left_idx -= 1
        right_idx += 1
    return [left_idx + 1, right_idx]
