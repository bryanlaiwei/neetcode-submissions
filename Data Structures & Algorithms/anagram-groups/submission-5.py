class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:  
            snapshotLst = [0] * 26

            for c in s:
                snapshotLst[ord(c) - ord('a')] += 1

            snapshotTp = tuple(snapshotLst)
            if snapshotTp not in d: d[snapshotTp] = [s]
            else: d[snapshotTp].append(s)
        
        res = []
        for key, value in d.items():
            res.append(value)
        
        return res
