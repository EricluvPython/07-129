class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        if len(s)%2 == 1:
            return False
        if s[-1] in ['(','[','{']:
            return False
        
        for i in s:
            if len(stk) > 0:
                if i in [')',']','}']:
                    if stk[-1] == '(' and i ==")":
                        stk.pop()
                    elif ord(i)-2 == ord(stk[-1]):
                        stk.pop()
                    else:
                        return False
                else:
                    stk.append(i)
            else:
                stk.append(i)

        if len(stk) == 0:
            return True
        else:
            return False
