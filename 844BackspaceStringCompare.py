class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sstack=list()
        tstack=list()
        for i in s:
            if i=='#':
                if len(sstack)!=0:
                    sstack.pop()
            else:
                sstack.append(i)
        for i in t:
            if i=='#':
                if len(tstack)!=0:
                    tstack.pop()
            else:
                tstack.append(i)
        return sstack==tstack
