"""
Permutation in a String (hard)#
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string.
For example, “abc” has the following six permutations:

>> abc
>> acb
>> bac
>> bca
>> cab
>> cba

pattern: sliding window

Algorithm

1. Create a HashMap to calculate the frequencies of all characters in the pattern
2. Iterate throught the string adding one character at a time int the sliding windown
3. If the character being added matches a character in the HashMap, decrement its freq in the map. If
the character frequency becomes zero, we got a complete match
4. if at any time the number of characters matched is equal to the number of distinct characters in the pattern (i.e
total characters in the HashMap), we have gotten our required permutationself.
5. If the window size is greater than the length of the pattern, shrink the window to make it equal to the
pattern's size. At the same time, if characters going out was part of the pattern, put it back in the frequency HashMap
"""

def find_permutation(s, pattern):

    freq = {}
    for c in pattern:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1

    start = 0
    matched = 0
    for end in range(len(s)):
        c = s[end]
        if c in freq:
            freq[c] -= 1
            if freq[c] == 0:
                matched += 1

        if matched == len(freq):
            return True

        if end >= len(pattern) - 1:
            left = s[start]
            start += 1
            if left in freq:
                if freq[left] == 0:
                    matched -= 1
                freq[left] += 1
    return False


assert True is find_permutation("oidbcaf", "abc")
assert False is find_permutation("odicf", "dc")
assert True is find_permutation("bcdxabcdy", "bcdyabcdx")
assert True is find_permutation("aaacb", "abc")
