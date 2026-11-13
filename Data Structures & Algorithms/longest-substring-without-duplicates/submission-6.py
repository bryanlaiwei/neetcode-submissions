class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = 0
        cur = 0
        res = 0

        for r in range(0, len(s)):
            if s[r] not in d or d[s[r]] < l: 
                d[s[r]] = r
                cur += 1
                res = max(res, cur)
            else:  
                # newL = d[s[r]] + 1
                cur -= (d[s[r]] + 1 - l - 1)
                l = d[s[r]] + 1
                
                d[s[r]] = r
        
        return res
        