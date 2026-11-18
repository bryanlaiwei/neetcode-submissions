class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        maxCount, l, res = 1, 0, 0

        for r in range(0, k):
            if s[r] not in d: d[s[r]] = 1
            else: 
                d[s[r]] += 1
                maxCount = max(d[s[r]], maxCount)
            
            if r - l + 1 <= k + maxCount: res = max(r - l + 1, res)
        
        for r in range(k, len(s)):
            if s[r] not in d: d[s[r]] = 1
            else: 
                d[s[r]] += 1
                maxCount = max(maxCount, d[s[r]])
        
            if not r - l + 1 <= k + maxCount:
                d[s[l]] -= 1
                l += 1
            
            res = max(r - l + 1, res)
        
        return res
        