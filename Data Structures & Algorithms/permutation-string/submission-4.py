class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        windowLen = len(s1)
        d = {}
        res = False
        s1Dict = {}
        for c in s1:
            if c not in s1Dict: s1Dict[c] = 1
            else: s1Dict[c] += 1

        for i in range(0, windowLen):
            if s2[i] not in d: d[s2[i]] = 1
            else: d[s2[i]] += 1
        
        print(s1Dict, d)
        res1 = True
        for key in s1Dict:
            print(key)
            if key not in d or d[key] != s1Dict[key]: 
                print("check failed", key, d, s1Dict)
                res1 = False
                print("break")
                break
        res = res1
        if res: 
            print("hi")
            return res


        for r in range(windowLen, len(s2)):
            if s2[r] not in d: d[s2[r]] = 1
            else: d[s2[r]] += 1

            l = r - windowLen
            if s2[l] in d and d[s2[l]] > 0: d[s2[l]] -= 1

            if s2[r] in s1Dict:
                print("check started")
                res1 = True
                for key in s1Dict:
                    # print(key, d[key], s1Dict[key])
                    if key not in d or d[key] != s1Dict[key]: 
                        print("check failed", key, d, s1Dict)
                        res1 = False
                        break
                res = res1
                if res: return res
            
            print(d, s1Dict)
        
        return res

            

            