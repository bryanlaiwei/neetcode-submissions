class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] 
        postfix = 1
        length = len(nums)

        for i in range(0, length - 1):
            res.append(nums[i] * res[-1])
        
        for i in range(length - 1, 0, -1):
            res[i] *= postfix
            postfix *= nums[i]

        res[0] *= postfix
        return res

        # 1 2 8 48
        # 6 24 48 48