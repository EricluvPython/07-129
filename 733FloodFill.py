class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        tcolor = image[sr][sc]
        def dfs(row, column):
            if image[row][column] == color: 
                return

            image[row][column] = color
            for i,j in directions:
                newr, newc = i+row, j+column
                if 0 <= newr < len(image) and 0 <= newc < len(image[0]) and image[newr][newc] == tcolor:
                    dfs(newr, newc)

        dfs(sr,sc)
        return image
