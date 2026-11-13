class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = 0
        res = 0

        for r in range(0, len(s)):
            if s[r] not in d or d[s[r]] < l: 
                d[s[r]] = r
            else:  
                l = d[s[r]] + 1
                d[s[r]] = r
            res = max(res, r - l + 1)
        
        return res
        