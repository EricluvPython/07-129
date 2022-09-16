class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        d = {}
        def solve(col,row):
            if row == len(triangle)-1:
                return triangle[row][col]
            if (col,row) in d:
                return d[(col,row)]
            d[(col,row)]=triangle[row][col]+min(solve(col,row+1),solve(col+1,row+1))
            return d[(col,row)]
        return solve(0,0)
