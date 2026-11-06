class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCountDict = {}
        countNumLst = []
        for i in range(len(nums) + 1):
            countNumLst.append([])
        
        for i in nums:
            if not (i in numCountDict): numCountDict[i] = 1  
            else: numCountDict[i] += 1
        for key, value in numCountDict.items():
            countNumLst[value].append(key)

        finalLst = []
        while (len(finalLst) < k):
            for key in range(len(nums), 0, -1):
                if (countNumLst[key] != []):
                    finalLst += countNumLst[key]
        
        return finalLst[:k]