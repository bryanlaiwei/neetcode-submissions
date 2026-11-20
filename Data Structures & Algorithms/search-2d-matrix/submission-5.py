class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        idx = 0

        while l <= r:
            m = l + (r - l) // 2

            if matrix[m][-1] < target: l = m + 1
            elif matrix[m][0] > target: r = m - 1
            else: 
                idx = m
                break
        
        l1, r1 = 0, len(matrix[idx]) - 1
        while l1 <= r1:
            m = l1 + (r1 - l1) // 2
            if matrix[idx][m] == target: return True
            elif matrix[idx][m] < target: l1 = m + 1
            else: r1 = m - 1
        
        return False