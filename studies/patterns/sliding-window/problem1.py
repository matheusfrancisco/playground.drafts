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
""" 

def solution(s, pattern):

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



assert True == solution("oidbcaf", "abc")
assert False == solution("odicf", "dc")
assert True == solution("bcdxabcdy", "bcdyabcdx")
assert True == solution("aaacb", "abc")
