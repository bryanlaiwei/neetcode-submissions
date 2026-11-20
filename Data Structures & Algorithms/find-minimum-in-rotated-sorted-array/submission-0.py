class Solution:
    def findMin(self, nums: List[int]) -> int:
        # from range 0, length - 1, we do a binary search
        # middle index corresponds to a number: 
        #       while l <= r
        #       l index number does not have a greater left neighbour and greater right neighbour:
        #       r jumps to middle index - 1 -> if that crosses l, swap r and l
        #       if we encounter negative index -> convert to length - abs(idx), so that we can compare left and right
        #       else: index l is the min we want
        
        l, r = 0, len(nums) - 1
        while l <= r:
            # if nums[l - 1] > nums[l]: 
            #     print("hello")
            #     return nums[l]
            # else:
            #     print("hi")
            m = (r + l) // 2
            if nums[m - 1] < nums[m]: 
                r = m - 1
                if r < l: 
                    r_copy = r
                    r = l
                    l = r_copy
            else: return nums[m]
