class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, res = 0, len(heights) - 1, 0

        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r - l))

            if heights[l] < heights[r]: 
                while heights[l] > heights[l + 1] and l < r: l += 1
                l += 1
            elif heights[l] > heights[r]: 
                while heights[r] > heights[r - 1] and l < r: r -= 1
                r -= 1
            else: 
                l += 1
                r -= 1
        
        return res
