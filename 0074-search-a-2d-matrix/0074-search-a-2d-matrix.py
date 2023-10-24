class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row 
        l, r = 0, len(matrix) - 1
        while l <= r: 
            m = (l + r) // 2
            if target < matrix[m][0]: 
                r = m - 1
            else: 
                l = m + 1
        rowToSearch = r
        l, r = 0, len(matrix[rowToSearch]) - 1    
        while l <= r: 
            m = (l + r) // 2
            if target < matrix[rowToSearch][m]:
                r = m - 1
            else: 
                l = m + 1
        return matrix[rowToSearch][r] == target
        