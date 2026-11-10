class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {} 
        for s in strs:
            snapshot = [0] * 26
            for c in s:
                snapshot[ord(c) - ord("a")] += 1
            tp = tuple(snapshot)
            if not d or tp not in d: d[tp] = [s]
            else: d[tp].append(s)
        
        return list(d.values())


        