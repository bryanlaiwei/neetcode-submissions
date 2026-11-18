class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        setNums = set(nums)
        res = 1
        for n in nums: 
            ncp = n
            if ncp - 1 not in setNums and ncp + 1 in setNums: 
                count = 1
                while ncp + 1 in setNums: 
                    count += 1
                    ncp += 1
                res = max(res, count)
        
        return res