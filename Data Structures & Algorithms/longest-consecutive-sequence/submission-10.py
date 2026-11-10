class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        numsSet = set()
        for n in nums: numsSet.add(n)

        res = 1
        for n in nums:
            if (n - 1) not in numsSet:
                m = n + 1
                while m in numsSet:
                    m += 1
                if m - n > res: res = m - n
        
        return res