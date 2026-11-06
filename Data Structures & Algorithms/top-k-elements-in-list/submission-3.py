class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCountDict = {}
        countNumDict = {}
        for i in range(len(nums) + 1):
            countNumDict[i] = []
        for i in nums:
            if not (i in numCountDict): numCountDict[i] = 1  
            else: numCountDict[i] += 1
        for key, value in numCountDict.items():
            countNumDict[value].append(key)

        finalLst = []
        for key in range(len(nums), 0, -1):
            finalLst += countNumDict[key]
            if len(finalLst) >= k:
                break
                
        return finalLst[:k]