class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = []
        suffix = []
        product = 1
        for i in range(0, length):
            product *= nums[i]
            prefix.append(product)
        product = 1
        for i in range(length - 1, -1, -1):
            product *= nums[i]
            suffix.append(product)

        res = []
        for i in range(0, length):
            if i == 0: product = suffix[length - 2]
            elif i == length - 1: product = prefix[i - 1]
            else: product = prefix[i - 1] * suffix[length - 2 - i]
            res.append(product)
        
        return res