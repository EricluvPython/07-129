class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        s = s.lower()
        def solve(index, combo, s):
            if index == len(s):
                ans.append(''.join(combo))
                return
            if s[index].isalpha():
                solve(index + 1, combo + [s[index].upper()], s)
            solve(index + 1, combo + [s[index]], s)
    
        solve(0, [], s)
        return ans
