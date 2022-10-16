class Solution:
    def divisor_substrings(self, num: int, k: int) -> int:
        count = 0
        num_str = str(num)
        end = 0
        while (end + k) <= len(num_str):
            n = num_str[end:end+k]
            if int(n) > 0 and num % int(n) == 0:
                count += 1
            end += 1
        return count
