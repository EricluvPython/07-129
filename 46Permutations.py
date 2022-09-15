class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def perm(L):
            if L == []:
                return [[]]
            perms = perm(L[1:])
            r = []
            for item in perms:
                for i in range(len(item)+1):
                    r.append(item[0:i]+[L[0]]+item[i:])
            return r
        return perm(nums)
