class Solution:
    def minimum_recolors(self, blocks: str, k: int) -> int:
        ans = num_w = blocks[:k].count("W")

        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                num_w += 1
            if blocks[i-k] == "W":
                num_w -= 1
            ans = min(ans, num_w)
        return ans
