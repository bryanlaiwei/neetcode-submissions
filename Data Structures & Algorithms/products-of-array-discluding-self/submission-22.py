class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i in range(len(nums) - 1):
            if i >= 1: res[i + 1] = nums[i] * res[i]
            else: res[i + 1] = nums[i]
        
        cur = 1
        for j in range(len(nums) - 1, 0, -1):
            # print(cur)
            cur *= nums[j]
            res[j - 1] *= cur

        # [0, 1, 2, 8]
        # [48, 24, 6, 0]

        return res