class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {} # snapshot tp: list of words
        for s in strs:
            snapshot = [0] * 26
            for c in s:
                idx = ord(c) - ord("a")
                snapshot[idx] += 1
            tp = tuple(snapshot)
            if not d or tp not in d: d[tp] = [s]
            else: d[tp].append(s)
        
        res = []
        for key in d:
            res.append(d[key])
        
        return res


        