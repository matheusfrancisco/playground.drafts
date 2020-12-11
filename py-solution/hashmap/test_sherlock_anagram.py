def get_all_substrings(string):
    substrings = [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)] # noqa
    return substrings


def is_anagram(s1, s2):
    hashmap = {}
    if len(s1) != len(s2):
        return False

    for idx in range(len(s1)):
        word = s1[idx]
        if hashmap.get(word):
            hashmap[word] += 1
        else:
            hashmap[word] = 1

    for idx in range(len(s2)):
        word = s2[idx]
        if hashmap.get(word):
            hashmap[word] -= 1
        else:
            return False
    return True


def sherlock(words):
    """
      Algorithm very slow # TODO improve this code
      get_all_substrings : TIME O(n^2)
      is_anagram : TIME O(n)

      TIME O(n^2 * n* log n)
    """
    substrings = get_all_substrings(words)
    count = 0
    for idx in range(len(substrings)):
        left = idx - 1
        right = idx + 1

        while (left >= 0):
            if is_anagram(substrings[idx], substrings[left]):
                count += 1
            left -= 1

        while (right < len(substrings)):
            if is_anagram(substrings[idx], substrings[right]):
                count += 1
            right += 1

    return count//2


def test_sherlock_anagrams():
    string = "abb"
    assert get_all_substrings("abb") == ["a", "ab", "abb", "b", "bb", "b"]
    assert is_anagram("ab", "ba") is True
    assert is_anagram("a", "ba") is False
    assert sherlock(string) == 1
