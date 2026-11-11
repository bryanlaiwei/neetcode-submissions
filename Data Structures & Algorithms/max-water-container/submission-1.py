class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        res = 0

        while i < j:
            lHeight, rHeight = heights[i], heights[j]
            res = max(res, (j - i) * min(lHeight, rHeight))
            if lHeight < rHeight:
                while i < j and heights[i] <= lHeight: i += 1
            elif rHeight < lHeight: 
                while i < j and heights[j] <= rHeight: j -= 1
            else: 
                while i < j and heights[i] <= lHeight: i += 1
                while i < j and heights[j] <= rHeight: j -= 1

        return res        