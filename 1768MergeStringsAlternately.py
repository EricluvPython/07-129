class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        if len(word1) <= len(word2):
            minLen = len(word1) 
        else:
            minLen = len(word2)
        for i in range(minLen):
            s += word1[i]+word2[i]
        return s + word1[minLen:] + word2[minLen:]
