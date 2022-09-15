class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        numbers = [i for i in range(1, n+1)]
        res = []
        cur = []
        
        def dfs(i):
            if len(cur) == k:
                res.append(cur.copy())
                return
            if i >= n:
                return
            cur.append(numbers[i])
            dfs(i+1)
            cur.pop()
            dfs(i+1)
        
        dfs(0)
        return res
