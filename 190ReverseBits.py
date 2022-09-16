class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f"{n:#034b}"[::-1][:-2],2)
