def isAnagram(self, s: str, t: str) -> bool:
    words_1 = [0]*27
    words = [0]*27
    for c in s:
        value = ord(c) - ord('a')
        old = words[value]
        words[value] = old + 1
    
    for c in t:
        value = ord(c) - ord('a')
        old = words_1[value]
        words_1[value] = old + 1
    
    return words_1 == words
