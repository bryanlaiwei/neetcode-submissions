class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = []
        suffix = []
        product = 1
        product2 = 1
        for i in range(0, length):
            product *= nums[i]
            prefix.append(product)
            product2 *= nums[length - 1 - i]
            suffix.append(product2)

        res = []
        for i in range(0, length):
            if i == 0: product = suffix[length - 2]
            elif i == length - 1: product = prefix[i - 1]
            else: product = prefix[i - 1] * suffix[length - 2 - i]
            res.append(product)
        
        return res