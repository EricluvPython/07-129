class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(len(coordinates)-2):
            x = coordinates[i][0]
            x1 = coordinates[i+1][0]
            x2 = coordinates[i+2][0]
            y = coordinates[i][1]
            y1 = coordinates[i+1][1]
            y2 = coordinates[i+2][1]
            if (x-x1)*(y2-y1) != (x2-x1)*(y-y1):
                return False
        return True
