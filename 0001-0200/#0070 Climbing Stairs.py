class Solution:
    def climbStairs(self, n: int) -> int:
        fib_dict = {
            1: 1,
            2: 2
        }

        for i in range(3, n + 1):
            fib_dict[i] = fib_dict[i - 1] + fib_dict[i - 2]

        return fib_dict[n]
