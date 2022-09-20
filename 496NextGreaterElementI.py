class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for i in nums1:
            started = False
            found = False
            for j in nums2:
                if j == i:
                    started = True
                if started and j > i:
                    output.append(j)
                    found = True
                    break
            if not found:
                output.append(-1)
        return output
