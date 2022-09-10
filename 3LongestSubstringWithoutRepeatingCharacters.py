class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        d = {}
        l = 0
        ans = 0
        for r in range(len(s)):
            rs = s[r]
            if rs in d:
                l = max(l, d[rs] + 1)
            d[rs] = r
            ans = max(ans, r-l+1)
        
        return ans
