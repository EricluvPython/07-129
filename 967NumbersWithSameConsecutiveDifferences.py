class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while n > 1:
            tmp = []
            for val in lst:
                rem = val % 10
                if rem + k < 10:
                    tmp.append(val * 10 + rem + k)
                if k != 0 and rem - k >= 0:
                    tmp.append(val * 10 + rem - k)
            lst = tmp
            n -= 1
        return lst
