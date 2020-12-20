
def two_strings(s1, s2):
    # TIME: O(m) + O(26), m is the max len of strinng
    # Space : O(2 * c), c = 26
    offset = ord('a')
    string1 = [False] * 26
    string2 = [False] * 26
    size = max(len(s1), len(s2))
    len1 = len(s1)
    len2 = len(s2)
    for i in range(size):
        if i < len1:
            string1[ord(s1[i]) - offset] = True
        if i < len2:
            string2[ord(s2[i]) - offset] = True
    for j in range(26):
        if string1[j] and string2[j]:
            return "YES"
    return "NO"


def test_two_strings():
    assert two_strings("hello", "world") == "YES"
    assert two_strings("hi", "world") == "NO"
