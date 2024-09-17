class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    # Optimal Solution
    # Strt from top-right
    # If the current element is smaller than the target, move down
    # If the current element is greter than the target, move left
        m = len(matrix)
        n = len(matrix[0])

        row = 0
        col = n - 1

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False
    # TC: O(m + n) we move either left or down, i the worst case we will move (m + n) times
    # SC: O(1)
    
    
    #     m = len(matrix)
    #     n = len(matrix[0])

    #     if target > matrix[m - 1][n - 1] or target < matrix[0][0]:
    #         return False
        
    # # BINARY SEARCH

    #     def find(row, target):
    #         if row >= m:
    #             return False

    #         l = 0
    #         r = n - 1

    #         if target > matrix[row][-1]:
    #             return find(row + 1, target)

    #         while l <= r:
    #             mid = (l + r) // 2
    #             if matrix[row][mid] == target:
    #                 return True
    #             elif matrix[row][mid] < target:
    #                 l = mid + 1
    #             else:
    #                 r = mid - 1
    #         return False
    #     return find(0, target)
    
    # # TC: O(m * log(n)) m rows and binary search on each row in worst case
    # # SC: O(1) space complexity is minimal, less that O(m) for recursive depth