class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] #prefix first, then times suffix
        suffix = [1]
        length = len(nums)

        for i in range(0, length - 1):
            res.append(nums[i] * res[-1])
        
        for i in range(length - 1, 0, -1):
            rMultiply = nums[i] * suffix[-1]
            res[i] *= suffix[-1]
            suffix.append(rMultiply)
        
        # print(res)
        # print(suffix)
        res[0] *= suffix[-1]
        return res

        # 1 2 8 48
        # 6 24 48 48