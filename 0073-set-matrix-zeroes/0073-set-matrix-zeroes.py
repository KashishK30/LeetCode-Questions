class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Optimal Approach
        m = len(matrix)
        n = len(matrix[0])

        # Variable to keep track of whether the 1st col should be zero
        col0 = 1

        # First pass: Mark row and col to be zeroed be using the first row and col
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # Set the 1st element of the row to 0
                    matrix[i][0] = 0
                    if j != 0:
                        # Set the 1st element of the col to 0
                        matrix[0][j] = 0
                    else:
                        # If the element is in the 1st col, mark col0 to be zeroed later
                        col0 = 0

        # Second pass: Zero out cells based on markers in the 1st row               
        for i in range(1, m): # Start from the second row
            for j in range(1, n): # Start from the second column
                # If the 1st element of the row and column is zero, set the current element to 0
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle the 1st row separately if it contains any zeroes
        if matrix[0][0] == 0:
            for j in range(1, n):
                matrix[0][j] = 0
        # Handle the 1st column based on the col0
        if col0 == 0:
            for i in range(m):
                matrix[i][0] = 0

        return matrix    
        


        # # Better Solution
        # m = len(matrix)
        # n = len(matrix[0])

        # row = [0] * m
        # col = [0] * n

        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             row[i] = 1
        #             col[j] = 1
        
        # for i in range(m):
        #     for j in range(n):
        #         if row[i] == 1:
        #             matrix[i][j] = 0
        #         if col[j] == 1:
        #             matrix[i][j] = 0
        
        # return matrix

        # # TC: O(m * n) + O(m * n) = O(2 * (m * n)
        # # SC: O(m) + O(n)

        # # Brute Force

        # m = len(matrix)
        # n = len(matrix[0])

        # def markRow(matrix, m, n, i):
        #     for j in range(n):
        #         if matrix[i][j] != 0:
        #             matrix[i][j] = -1
                

        # def markCol(matrix, m, n, j):
        #     for i in range(m):
        #         if matrix[i][j] != 0:
        #             matrix[i][j] = -1
                

        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             markRow(matrix, m, n, i)
        #             markCol(matrix, m, n, j) 
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == -1:
        #             matrix[i][j] = 0

        # return matrix

        # # TC: O((m * n) * (m + n)) + O(m * n)
        # # O(m * n) Traversing the matrix to find the cells with the value 0
        # # O(m + n) Whenever we find any such cell, we make the entire row and column with -1 except the one with 0
        # # O( * n) to mark all the cells with from -1 to 0
        # # SC: O(1)