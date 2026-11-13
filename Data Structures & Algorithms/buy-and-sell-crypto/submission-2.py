class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0

        for r in range(1, len(prices)):
            while l < r:
                if l >= 1 and prices[l - 1] <= prices[l]: 
                    l += 1
                    continue
                if prices[r] - prices[l] > res: res = prices[r] - prices[l]
                l += 1
            l = 0
        
        return res