class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sumn = 0
        for i in str(n):
            prod *= int(i)
            sumn += int(i)
        return prod-sumn
