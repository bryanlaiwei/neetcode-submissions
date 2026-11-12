class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [], []
        length = len(nums)

        for i in range(0, length):
            if not prefix: prefix.append(nums[i])
            else: prefix.append(nums[i] * prefix[-1])

            if not suffix: suffix.append(nums[length - 1 - i])
            else: suffix.append(nums[length - 1 - i] * suffix[-1])
        
        res = []
        for i in range(0, length): 
            if i == 0: res.append(suffix[length - 2])
            elif i == length - 1: res.append(prefix[length - 2])
            else: res.append(prefix[i - 1] * suffix[length - 2 - i])
        
        return res