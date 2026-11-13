class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0

        for r in range(1, len(prices)):
            while l < r:
                if prices[r] - prices[l] > res: res = prices[r] - prices[l]
                l += 1
            l = 0
        
        return res