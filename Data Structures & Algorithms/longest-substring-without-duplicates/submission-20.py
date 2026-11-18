class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l, res = 0, 0

        for r in range(len(s)):
            if s[r] not in d: d[s[r]] = 1
            elif d[s[r]] == 0: d[s[r]] = 1
            elif d[s[r]] == 1:         
                while d[s[r]] == 1:
                    d[s[l]] = 0
                    l += 1
                d[s[r]] = 1
            
            res = max(res, r - l + 1)

            # print(l, r, res, d)
        
        return res

        