class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairDict = {}
        
        for i in range(0, len(nums)):
            if (nums[i] in pairDict): return [pairDict[nums[i]], i]
            pairDict[target - nums[i]] = i
            
        