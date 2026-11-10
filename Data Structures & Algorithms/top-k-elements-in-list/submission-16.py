class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if not count or n not in count: count[n] = 1
            else: count[n] += 1
        
        revCount = {}
        for i in range(1, len(nums) + 1):
            revCount[i] = []
        
        for key, value in count.items():
            revCount[value].append(key)
        
        res = []
        count = 0
        for i in range(len(nums), 0, -1):
            if revCount[i]: 
                count += 1
                res.extend(revCount[i])
                print(res)
            
            if count == k: return res[0:k]
        
        return res[0:k]