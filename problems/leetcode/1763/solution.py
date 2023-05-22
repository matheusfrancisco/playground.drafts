class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        char_set = set(s)
        if len(s) < 2:
            return ""
        for idx, char in enumerate(s):
            if char.swapcase() not in char_set:
                s1 = self.longestNiceSubstring(s[0:idx])
                s2 = self.longestNiceSubstring(s[idx+1:])

                if len(s2) > len(s1):
                    return s2
                else:
                    return s1
        return s


if __name__ == '__main__':
    assert "" == Solution().longestNiceSubstring("YazaAay")
