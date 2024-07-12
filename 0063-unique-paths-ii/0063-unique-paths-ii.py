class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0] * n

        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        if obstacleGrid[0][0] == 0:
            dp[0] = 1
        
        for j in range(1, n):
            dp[j] = dp[j - 1] if obstacleGrid[0][j] == 0 else 0

        for i in range(1, m):
            dp[0] = dp[0] if obstacleGrid[i][0] == 0 else 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[j] += dp[j - 1]
                else:
                    dp[j] = 0
        return dp[n - 1]