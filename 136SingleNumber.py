class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = list(set(nums)) * 2
        for i in a:
            try:
                nums.remove(i)
            except ValueError:
                return i
