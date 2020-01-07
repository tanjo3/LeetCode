class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(map(int, f"{n:b}"))
