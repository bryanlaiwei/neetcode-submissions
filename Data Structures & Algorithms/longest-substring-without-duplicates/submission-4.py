class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = 0
        res = 0

        for r in range(0, len(s)):
            if s[r] not in d: 
                d[s[r]] = r
                res = max(res, len(d))
            else:  
                newL = d[s[r]] + 1
                for i in range(l, newL): 
                    del d[s[i]]
                l = newL
                d[s[r]] = r
        
        return res

# a 0, b 1, c 2
# newL = 3
# abcabcbb
        