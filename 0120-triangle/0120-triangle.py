class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ## MEMOIZATION
        # n = len(triangle)
        # memo = {}

        # def dfs(row, col):
        #     if row == n - 1:
        #         return triangle[row][col]
        #     if (row, col) in memo:
        #         return memo[(row, col)]
            
        #     left = dfs(row + 1, col)
        #     right = dfs(row + 1, col + 1)
        #     memo[(row, col)] = triangle[row][col] + min(left, right)
        #     return memo[(row, col)]
        # return dfs(0, 0)

        ## TABULATION
        n = len(triangle)
        dp = [[0] * len(row) for row in triangle]

        for col in range(len(triangle[-1])):
            dp[-1][col] = triangle[-1][col]
        
        for row in range(n - 2, -1, -1):
            for col in range(len(triangle[row])):
                dp[row][col] = triangle[row][col] + min(dp[row + 1][col], dp[row + 1][col + 1])
        return dp[0][0]


        
            