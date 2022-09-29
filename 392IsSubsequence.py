class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        cnt=0
        for i in range(0,len(t)):
            if cnt <= len(s) -1:
                if s[cnt] == t[i]:
                    cnt+=1
        return  cnt == len(s) 
