class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        snapshots = {}

        for s in strs:
            snapshot = [0] * 26

            for c in s:
                snapshot[ord(c) - 97] += 1

            snapshottp = tuple(snapshot)

            if snapshottp not in snapshots:
                snapshots[snapshottp] = []

            snapshots[snapshottp].append(s)
        
        final = []
        for key in snapshots: 
            final.append(snapshots[key])
        
        return final
        