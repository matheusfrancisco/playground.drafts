

"""
Given a string find the length of the longest substring which has all ditinct characters:
Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring with distinct characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring with distinct characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings with distinct characters are "abc" & "cde".
"""

def solution(s):
    start = 0
    char_index = {}
    max_length = 0
    for end in range(len(s)):
        c = s[end]
        if c in char_index:
            start = max(start, char_index[c] + 1)

        max_length = max(max_length, end - start + 1)
        char_index[c] = end
    return max_length

assert 3 == solution("aabccbb")
