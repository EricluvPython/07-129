class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s1=""
        s2=""
        x=0
        for i in range(len(secret)):  
            if secret[i]==guess[i]:
                x+=1
            else:
                s1=s1+secret[i] 
                s2=s2+guess[i] 
        y=0 
        for i in range(len(s1)): 
            if s1[i] in s2:
                y+=1
                s2=s2.replace(s1[i],'',1)
        return str(x)+"A"+str(y)+"B"
