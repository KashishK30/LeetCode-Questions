class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = {}

        def backtrack(i, j):

            if i < 0 or j < 0:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            
            up = backtrack(i - 1, j)
            left = backtrack(i, j - 1)
            memo[(i, j)] = up + left

            return memo[(i, j)]

        return backtrack(m - 1, n - 1)
