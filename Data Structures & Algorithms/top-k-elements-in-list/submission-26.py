class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        dRev = {}

        for i in nums:
            if i not in d: d[i] = 1
            else: d[i] += 1
        
        for i in range(1, len(nums) + 1):
            dRev[i] = []
        
        for key in d:
            dRev[d[key]].append(key)
        
        res = []
        while len(res) < k:
            for i in range(len(nums), 0, -1):
                if dRev[i]: res.extend(dRev[i])
        
        return res[0:k]