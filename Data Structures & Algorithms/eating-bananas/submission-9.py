class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            curH = 0
            curK = l + (r - l) // 2
            for pile in piles:
                curH += (pile + curK - 1) // curK
        
            if curH > h: l = curK + 1
            else: r = curK
        
        return l
