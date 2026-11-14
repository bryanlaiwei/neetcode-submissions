class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        windowLen = len(s1)
        matchChar = 0
        res = False
        s1Dict = {}

        for c in s1:
            if c not in s1Dict: s1Dict[c] = 1
            else: s1Dict[c] += 1
        
        s1DictLen = len(s1Dict)

        for i in range(0, windowLen):
            if s2[i] in s1Dict: 
                s1Dict[s2[i]] -= 1
                if s1Dict[s2[i]] == 0: matchChar += 1
                elif s1Dict[s2[i]] == -1: matchChar -= 1
            
            if matchChar == s1DictLen: return True

        for r in range(windowLen, len(s2)):
            if s2[r] in s1Dict: 
                s1Dict[s2[r]] -= 1
                if s1Dict[s2[r]] == 0: matchChar += 1
                elif s1Dict[s2[r]] == -1: matchChar -= 1

            l = r - windowLen
            if s2[l] in s1Dict: 
                s1Dict[s2[l]] += 1
                if s1Dict[s2[l]] == 1: matchChar -= 1
                elif s1Dict[s2[l]] == 0: matchChar += 1

            if s2[r] in s1Dict and matchChar == s1DictLen: return True
        
        return False

            

            