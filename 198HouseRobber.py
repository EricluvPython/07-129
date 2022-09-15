class Solution:
    def rob(self, nums: List[int]) -> int:
      @lru_cache
        def findBestRob(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + findBestRob(i+2), findBestRob(i+1))
        return findBestRob(0)
