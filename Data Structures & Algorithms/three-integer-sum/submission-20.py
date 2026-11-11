class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = nums
        sortedNums.sort()
        res = []

        if sortedNums[0] > 0: return []

        for i in range(0, len(nums)):
            if sortedNums[i] > 0: break
            if i > 0 and nums[i] == nums[i - 1]: continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                n = sortedNums[i] + sortedNums[j] + sortedNums[k]
                if n > 0: k -= 1
                elif n < 0: j += 1
                else: 
                    res.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]: 
                        j += 1
        
        return res