class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        track = set()
        for n in nums:
            track.add(n)
        
        res = []
        for i in range(1, len(nums) + 1): 
            if i not in track: res.append(i)

        return res        