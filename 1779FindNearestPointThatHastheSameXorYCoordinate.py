class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        s = 999999999
        ans = -1
        for i,p in enumerate(points):
            a = p[0]
            b = p[1]
            if x == a or y == b:
                d = abs(x-a)+abs(y-b)
                if d < s:
                    s = d
                    ans = i
        return ans
