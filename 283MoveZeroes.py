class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        ans = []
        for i in range(len(nums)):
            if nums[i]==0:
                cnt += 1
        for i in range(len(nums)):
            if nums[i]!=0:
                ans.append(nums[i])
        for i in range(cnt):
            ans.append(0)
        nums[:] = ans
                
