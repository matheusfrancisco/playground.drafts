"""
  Write a function that takes in an array of strings
  and groups anagrams together anagrams are strings
  made up of exactly the same letters, where order doesn't matter,
  for example "cinema" and "iceman" are anagrams

  you function should return a list of anagram group in no particular order.
"""


def test_group_anagrams():
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    expected = [['act', 'tac', 'cat'], ['flop', 'olfp'], ['foo'], ['yo', 'oy']]
    assert group_anagrams(words) == expected


def group_anagrams(words):
    """Time: O(w * n * log(n) + n * w * log(w))
    Space: O(w * n * log(n))
    """
    sorted_words = ["".join(sorted(w)) for w in words]
    indices = [i for i in range(len(words))]
    indices.sort(key=lambda x: sorted_words[x])
    result = []
    current_anagram_group = []
    current_anagram = sorted_words[indices[0]]
    for index in indices:
        word = words[index]
        sorted_word = sorted_words[index]
        if sorted_word == current_anagram:
            current_anagram_group.append(word)
            continue

        result.append(current_anagram_group)
        current_anagram_group = [word]
        current_anagram = sorted_word
    result.append(current_anagram_group)
    return result


def test_group_anagrams_hash():
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    expected = [['yo', 'oy'], ['act', 'tac', 'cat'], ['flop', 'olfp'], ['foo']]
    assert group_anagrams_hash(words) == expected


def group_anagrams_hash(words):
    """Time: O(w * n * log(n))
    Space: O(w * n )
    """
    anagrams = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())
