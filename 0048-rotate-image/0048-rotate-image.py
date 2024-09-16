class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse the matrix
        for i in range(n):
            matrix[i].reverse()
        
        return matrix
        
    # TC: O(n * n) for transposing
    # O(n * n) for reversing
    # Overall TC: O(n * n)

    # SC: O(1)