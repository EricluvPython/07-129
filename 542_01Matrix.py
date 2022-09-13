class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                if cell:
                    if i:
                        top = mat[i-1][j]
                    else:
                        top = float('inf')
                    if j:
                        left = mat[i][j-1]
                    else:
                        left = float('inf')
                    mat[i][j] = min(top, left) + 1
        for i in reversed(range(rows)):
            for j in reversed(range(cols)):
                if cell := mat[i][j]:
                    if i < rows-1:
                        bottom = mat[i+1][j]
                    else:
                        bottom = float('inf')
                    if j < cols-1:
                        right = mat[i][j+1]
                    else:
                        right = float('inf')
                    mat[i][j] = min(cell, bottom + 1, right + 1)
        return mat
