class Solution:
    def findMin(self, nums: List[int]) -> int:     
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if nums[m - 1] < nums[m]: 
                r = m - 1
                if r < l: 
                    r_copy = r
                    r = l
                    l = r_copy
            else: return nums[m]
