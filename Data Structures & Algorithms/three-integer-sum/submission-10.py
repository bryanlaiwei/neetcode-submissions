class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = nums
        sortedNums.sort()
        res = []
        s = set()

        if sortedNums[0] > 0: return []

        for i in range(0, len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                n = sortedNums[i] + sortedNums[j] + sortedNums[k]
                if n > 0: k -= 1
                elif n < 0: j += 1
                else: 
                    if (sortedNums[i], sortedNums[j], sortedNums[k]) not in s:
                        res.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                        s.add((sortedNums[i], sortedNums[j], sortedNums[k]))
                    # print(i, j, k)
                    j += 1
        
        return res
        

        # [-4, -1, -1, 0, 1, 2]