class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)
        for i in s1:
            d1[i] += 1
            
        l,r = 0,len(s1)

        while r < len(s2)+1:
            d2 =  defaultdict(int)
            for j in s2[l:r]:
                d2[j] += 1
            if d1 == d2:
                return True
            l += 1
            r += 1
        return False
