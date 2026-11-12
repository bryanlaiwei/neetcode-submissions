class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        repeat = set()

        for i in range(0, len(nums) - 2):
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0: 
                    if (nums[i], nums[j], nums[k]) not in repeat: res.append([nums[i], nums[j], nums[k]])
                    repeat.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif total < 0: 
                    while j < k and nums[j] == nums[j + 1]: 
                        j += 1
                    j += 1
                else: 
                    while j < k and nums[k] == nums[k - 1]: k -= 1
                    k -= 1
        
        return res