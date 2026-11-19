class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] == target or row[-1] == target: return True
            if row[0] < target and row[-1] > target:
                l, r = 0, len(row) - 1
                while l <= r:
                    m = l + (r - l) // 2
                    if row[m] < target: l = m + 1
                    elif row[m] > target: r = m - 1
                    else: return True     
                break
        
        return False