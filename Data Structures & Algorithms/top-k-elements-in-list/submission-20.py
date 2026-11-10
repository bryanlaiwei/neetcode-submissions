class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if not count or n not in count: count[n] = 1
            else: count[n] += 1
        
        revCount = [[] for i in range(len(nums))]

        for key, value in count.items():
            revCount[value - 1].append(key)

        res = []
        for i in range(len(nums) - 1, -1, -1):
            if revCount[i]: 
                res.extend(revCount[i])
            
            if len(res) == k: return res[0:k]
        
        return res[0:k]