class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        numSet = set(nums)
        res = 1
        for i in numSet:
            if i - 1 not in numSet and i + 1 in numSet:
                length = 1
                while i + length in numSet:
                    length += 1
                if length > res: res = length
        
        return res