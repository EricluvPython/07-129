class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for x in words:
            d[x] = d.get(x,0)+1
        res = sorted(d, key=lambda x: (-d[x], x))
        return res[:k]
