class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = -1
        for i in accounts:
            most = sum(i)
            if sum(i) > ans:
                ans = most
        return ans
