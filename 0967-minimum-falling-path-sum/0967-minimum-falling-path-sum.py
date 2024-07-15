class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ## TABULATION
        
        m = len(matrix)
        n = len(matrix[0])

        if not matrix or not matrix[0]:
            return 0

        dp = [row[:] for row in matrix]
        
        for row in range(1, m):
            for col in range(n):
                if col == 0:
                    dp[row][col] += min(dp[row - 1][col], dp[row - 1][col + 1])
                elif col == n - 1:
                    dp[row][col] += min(dp[row - 1][col], dp[row - 1][col - 1]) 
                else:
                    dp[row][col] += min(dp[row - 1][col - 1], dp[row - 1][col], dp[row - 1][col + 1])
        
        return min(dp[-1])