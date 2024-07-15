class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ## MEMOIZATION
        
        # if not matrix or not matrix[0]:
        #     return 0
        # m = len(matrix)
        # n = len(matrix[0])

        # memo = [[None] * n for _ in range(m)]

        # def dp(row, col):
        #     if col < 0 or col >= n:
        #         return float('inf')
        #     if row == 0:
        #         return matrix[0][col]
        #     if memo[row][col] is not None:
        #         return memo[row][col]
            
        #     memo[row][col] = matrix[row][col] + min(
        #         dp(row - 1, col),
        #         dp(row - 1, col - 1) if col > 0 else float('inf'),
        #         dp(row - 1, col + 1) if col < n - 1 else float('inf')
        #     )
        #     return memo[row][col]

        # return min(dp(m - 1, col) for col in range(n))

        # TC: (m*n), SC: (m*n)


        ## TABULATION

        # m = len(matrix)
        # n = len(matrix[0])

        # if not matrix or not matrix[0]:
        #     return 0

        # dp = [row[:] for row in matrix]
        
        # for row in range(1, m):
        #     for col in range(n):
        #         if col == 0:
        #             dp[row][col] += min(dp[row - 1][col], dp[row - 1][col + 1])
        #         elif col == n - 1:
        #             dp[row][col] += min(dp[row - 1][col], dp[row - 1][col - 1]) 
        #         else:
        #             dp[row][col] += min(dp[row - 1][col - 1], dp[row - 1][col], dp[row - 1][col + 1])
        
        # return min(dp[-1])

        # TC: (m*n), SC: (m*n)

        ## SPACE OPTIMIZATION

        if not matrix or not matrix[0]:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        prev = matrix[0][:]

        for row in range(1, m):
            curr = [0] * n
            for col in range(n):
                if col == 0:
                    curr[col] = matrix[row][col] + min(prev[col], prev[col + 1])
                elif col == n - 1:
                    curr[col] = matrix[row][col] + min(prev[col], prev[col - 1])
                else:
                    curr[col] = matrix[row][col] + min(prev[col], prev[col - 1], prev[col + 1])
            prev = curr
        
        return min(prev)

        # TC: O(m*n), SC: O(N)


