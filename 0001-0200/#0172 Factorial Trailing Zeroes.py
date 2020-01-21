class Solution:
    def trailingZeroes(self, n: int) -> int:
        num_zeros = 0

        while n >= 5:
            n = n // 5
            num_zeros += n

        return num_zeros
