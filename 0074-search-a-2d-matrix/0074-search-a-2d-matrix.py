class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        if target > matrix[m - 1][n - 1] or target < matrix[0][0]:
            return False
        
        def find(row, target):
            if row >= m:
                return False

            l = 0
            r = n - 1

            if target > matrix[row][-1]:
                return find(row + 1, target)

            while l <= r:
                mid = (l + r) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        return find(0, target)