class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if not s: return 0
        charSet = set()
        l, res = 0, 0

        for r in range(len(s)):
            if s[r] not in charSet: charSet.add(s[r])
            else: 
                
                while s[r] in charSet:
                    
                    # print(s[l])
                    charSet.remove(s[l])
                    l += 1
                charSet.add(s[r])
            
            res = max(res, r - l + 1)
            
            # print(l, r, res, charSet)
        
        return res

        