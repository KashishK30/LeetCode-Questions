class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Better Solution
        m = len(matrix)
        n = len(matrix[0])

        row = [0] * m
        col = [0] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        
        for i in range(m):
            for j in range(n):
                if row[i] == 1:
                    matrix[i][j] = 0
                if col[j] == 1:
                    matrix[i][j] = 0
        
        return matrix

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