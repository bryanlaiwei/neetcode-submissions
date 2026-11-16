class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res, maxCount = 0, 0, 0
        d = {}
        for r in range(0, len(s)):
            if s[r] not in d: d[s[r]] = 1
            else: d[s[r]] += 1

            maxCount = max(d[s[r]], maxCount)

            if r - l + 1 - k > maxCount:
                d[s[l]] -= 1
                l += 1
            else:
                res = max(res, r - l + 1)
                  
        return res

        