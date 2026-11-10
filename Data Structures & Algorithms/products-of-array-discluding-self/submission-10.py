class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = []
        suffix = []

        for i in range(0, length):
            if not prefix: prefix.append(nums[i])
            if not suffix: suffix.append(nums[length - i - 1])
            else: 
                prefix.append(prefix[-1] * nums[i])
                suffix.append(suffix[-1] * nums[length - i - 1])
        
        # for i in range(length - 1, -1, -1):
        #     if not suffix: suffix.append(nums[i])
        #     else: suffix.append(suffix[-1] * nums[i])

        res = []
        for i in range(0, length):
            if i == 0: res.append(suffix[length - 2])
            elif i == length - 1: res.append(prefix[length - 2])
            else: res.append(prefix[i - 1] * suffix[length - i - 2])
        
        return res