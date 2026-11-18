class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        d, l, matchCount = {}, 0, 0

        for c in s1:
            if c not in d: d[c] = 1
            else: d[c] += 1
        
        for i in range(0, len(s1)):
            if s2[i] in d: 
                d[s2[i]] -= 1
                if d[s2[i]] == 0: matchCount += 1
                elif d[s2[i]] < 0: matchCount -= 1
            
            matchCount = max(0, matchCount)    
            if matchCount == len(d): return True
            
        
        for r in range(len(s1), len(s2)):
            if s2[r] in d: 
                d[s2[r]] -= 1
                if d[s2[r]] == 0: matchCount += 1
                elif d[s2[r]] == -1: matchCount -= 1
            
            if s2[l] in d:
                d[s2[l]] += 1
                if d[s2[l]] == 0: matchCount += 1
                elif d[s2[l]] == 1: matchCount -= 1
            l += 1
            
            matchCount = max(0, matchCount)         
            if matchCount == len(d): return True
        
        return False
            
            


        
