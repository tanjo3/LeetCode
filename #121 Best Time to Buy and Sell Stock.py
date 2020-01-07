class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = float("inf")
        best_profit = 0

        for p in prices:
            min_p = min(p, min_p)
            if p - min_p > best_profit:
                best_profit = p - min_p

        return best_profit
