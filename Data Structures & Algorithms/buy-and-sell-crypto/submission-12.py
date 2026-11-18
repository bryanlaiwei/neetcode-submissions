class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, l = 0, 0

        for r in range(0, len(prices)):
            profit = prices[r] - prices[l]
            res = max(res, profit)

            if prices[r] < prices[l]: l = r
        
        return res