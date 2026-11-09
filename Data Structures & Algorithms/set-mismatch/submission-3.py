class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        track = {}
        res = [0, 0]
        for num in nums:
            if num not in track: track[num] = 1
            else: track[num] += 1
        
        for i in range(1, len(nums) + 1):
            if i not in track: res[1] = i
            elif track[i] == 2: res[0] = i
        
        return res
        