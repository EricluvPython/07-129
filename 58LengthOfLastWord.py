class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        keys = s.split()
        return len(keys[len(keys)-1])
