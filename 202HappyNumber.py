class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 2 or n == 3 or n == 4:
            return False
        def solve(total):
            ans = []
            my_list = [int(x) for x in str(n)]
            for x in my_list:
                x = x*x
                ans.append(x)
            total = sum(ans)
            if total == 1:
                return True
            elif total !=1:
                return Solution.isHappy (self, total)
            else:
                return False
        return solve(0)
