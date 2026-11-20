class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] <= nums[r]: return nums[l]

        while l < r:
            m = (r + l) // 2
            if nums[m] < nums[m - 1]: return nums[m]
            elif nums[m] <= min(nums[l], nums[r]): r = m - 1
            elif nums[m] >= max(nums[l], nums[r]): l = m + 1
            else: 
                if nums[m] > nums[l]: r = m - 1
                else: l = m + 1
        
        return nums[l]