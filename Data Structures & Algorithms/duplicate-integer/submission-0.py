class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            if i in dict:
                return True
            else:
                dict[i] = 0
        return False
        