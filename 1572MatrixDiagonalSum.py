class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        rows, cols = len(mat), len(mat[0])
        for i in range(rows):
            for j in range(cols):
                if i==j or i==cols-j-1:
                    ans += mat[i][j]
        return ans
        
