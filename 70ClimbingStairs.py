class Solution:
    def climbStairs(self, n: int) -> int:
        d = {0:0,1:1,2:2}
        ans = 0
        for i in range(3,n+1):
            d[i] = d[i-1] + d[i-2]
        return d[n]
