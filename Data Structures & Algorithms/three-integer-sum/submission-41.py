class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i >= 1 and nums[i] == nums[i - 1]: continue
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0: 
                    while nums[k] == nums[k - 1] and j < k: k -= 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    while nums[j] == nums[j + 1] and j < k: j += 1
                    j += 1
                else: 
                    res.append([nums[i], nums[j], nums[k]])
                    while nums[k] == nums[k - 1] and j < k: k -= 1
                    while nums[j] == nums[j + 1] and j < k: j += 1
                    k -= 1
                    j += 1
        
        return res

        
