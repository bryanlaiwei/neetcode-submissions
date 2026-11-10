class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        numsSet = set(nums)

        res = 1
        for n in nums:
            if (n - 1) not in numsSet:
                m = n + 1
                while m in numsSet:
                    m += 1
                res = max(m - n, res)
        
        return res