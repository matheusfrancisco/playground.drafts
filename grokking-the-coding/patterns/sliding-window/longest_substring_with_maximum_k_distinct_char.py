"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.


Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

Example 4:

Input: String="cbbebi", K=10
Output: 6
Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".
"""

"""
solution:
First, we will insert characters from the beginning of the string until we have K distinct characters in the HashMap.
These characters will constitute our sliding window. We are asked to find the longest such window having no more than K distinct characters. We will remember the length of this window as the longest window so far.
After this, we will keep adding one character in the sliding window (i.e., slide the window ahead) in a stepwise fashion.
In each step, we will try to shrink the window from the beginning if the count of distinct characters in the HashMap is larger than K. We will shrink the window until we have no more than K distinct characters in the HashMap. This is needed as we intend to find the longest window.
While shrinking, we’ll decrement the character’s frequency going out of the window and remove it from the HashMap if its frequency becomes zero.
At the end of each step, we’ll check if the current window length is the longest so far, and if so, remember its length.

Time complexity O(N)
Space O(N)
"""


def solution(s, k):

    start = 0
    max_len = 0
    freq = {}

    for end in range(len(s)):
        right_char = s[end]
        if right_char not in freq:
            freq[right_char] = 0
        freq[right_char] += 1

        while len(freq) > k:
            left_char = s[start]
            freq[left_char] -= 1

            if freq[left_char] == 0:
                del freq[left_char]

            start += 1

        max_len = max(max_len, end - start + 1)
    return max_len


assert 4 == solution("araaci", 2)

