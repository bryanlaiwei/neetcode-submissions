class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        prevDict = {}
        nextDict = {}
        l = []

        if nums == []: return 0

        for i in nums:
            if i not in prevDict: prevDict[i] = i - 1
            if i not in nextDict: nextDict[i] = i + 1

        for key in prevDict:
            if ((prevDict[key] not in nextDict) & (key in nextDict)):
                l.append(key)
        
        res = 1
        for i in l:
            length = 1
            while i + length in nextDict:
                length += 1
            if length > res: res = length

        return res

        