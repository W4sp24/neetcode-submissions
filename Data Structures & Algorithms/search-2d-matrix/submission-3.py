class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        total = m * n

        l ,r  = 0 , total - 1
        

        while l <= r:
            m =  (l + r) // 2
            i = m // n
            j = m % n

            middle_val = matrix[i][j]

            if middle_val == target:
                return True
            elif middle_val < target:
                l = m + 1
            else:
                r = m - 1
        return False
