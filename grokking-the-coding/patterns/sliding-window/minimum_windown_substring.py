"""
Statement#
    We are given two strings—s and t. 
    We have to find the smallest window substring of t. 
    The smallest window substring is the shortest sequence of 
    characters in s that includes all of the characters present 
    in t. The frequency of each character in this sequence should 
    be greater than or equal to the frequency of each character in 
    t. The order of the characters does not matter here.

"""

def min_window(s, t):
    start = 0
    t_count = {}
    for c in t:
        t_count[c] = 1 + t_count.get(c, 0)

    wind = {}
    ans, ans_len = [-1, -1], float("inf")

    for end in range(len(s)):
        current = s[end]

        if current in t_count:
            if current not in wind:
                wind[current] = 0
            wind[current] += 1

        while len(wind) == len(t_count):
            if (end - start + 1) < ans_len:
                ans = [start, end]
                ans_len = (end - start + 1)

            if s[start] in t_count:
                wind[s[start]] -= 1

                if wind[s[start]] == 0:
                    del wind[s[start]]

            start += 1
    start, end = ans
    if ans_len == float("inf"):
        return ""
    return s[start:end+1]
