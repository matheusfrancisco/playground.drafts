def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    words = {}
    for n in nums:
        v = words.get(n,0)
        if v == 0:
            words[n] = 1
        else:
            words[n] = v + 1
    
    d = sorted(words, key=words.get, reverse=True)
    out = []
    for i in range(k):
        out.append(d[i])
    return out
