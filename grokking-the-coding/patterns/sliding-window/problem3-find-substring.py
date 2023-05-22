"""doc
Smallest Window containing Substring (hard)#
Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="aabdec", Pattern="abac"
Output: "aabdec"
Explanation: The smallest substring having all character occurrences of the pattern is "aabdec"
Example 3:

Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".
Example 4:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.


Algo
1. We will keep a running count of every matching instance of a character.

2. Whenever we have matched all the characters, we will try to shrink the
window from the beginning, keeping track of the smallest substring that 
has all the matching characters.

3. We will stop the shrinking process as soon as we remove a matched character from 
the sliding window. One thing to note here is that we could have 
redundant matching characters, e.g., we might have two ‘a’ in the sliding window 
when we only need one ‘a’. In that case, when we encounter the first ‘a’, 
we will simply shrink the window without decrementing the matched count. We will
decrement the matched count when the second ‘a’ goes out of the window.

"""

def find_substring(str1, pattern):
    window_start = matched = substr_start = 0
    char_frequency = {}
    min_len = len(str1) + 1

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0:  # COUNT EVERY MATCH
                matched += 1

        while matched >= len(pattern):
            if min_len > window_end - window_start + 1:
                min_len = window_end - window_start + 1
                substr_start = window_start

            left_char = str1[window_start]
            window_start += 1

            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    if min_len > len(str1):
        return ""
    return str1[substr_start:substr_start + min_len]


assert "abdec" == find_substring("aabdec", "abc")

def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("aabdec", "abac"))
    print(find_substring("abdbca", "abc"))
    print(find_substring("adcad", "abc"))


main()
