class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = nums
        sortedNums.sort()
        res = set()

        if sortedNums[0] > 0: return []

        for i in range(0, len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                n = sortedNums[i] + sortedNums[j] + sortedNums[k]
                if n > 0: k -= 1
                elif n < 0: j += 1
                else: 
                    if (sortedNums[i], sortedNums[j], sortedNums[k]) not in res:
                        res.add((sortedNums[i], sortedNums[j], sortedNums[k]))
                    j += 1
        
        res2 = []
        for each in res:
            res2.append(list(each))

        return res2