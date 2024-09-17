class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    # SPACE OPTIMIZATION
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]
        return dp[-1]
    # TC: O(m * n)
    # SC: O(n)

    # # SPACE OPTIMIZATION
    #     curr = [1] * n
    #     prev = [1] * n

    #     for i in range(1, m):
    #         for j in range(1, n):
    #             curr[j] = prev[j] + curr[j - 1]
    #         curr, prev = prev, curr
    #     return  prev[n - 1]
    # # TC: O(m * n)
    # # SC: O(n)

    # # TABULATION
    #     dp = [[0 for _ in range(n)] for _ in range(m)]

    #     if m == 1 or n == 1:
    #         return 1
        
    #     for i in range(1, m):
    #         dp[i][0] = 1
        
    #     for j in range(1, n):
    #         dp[0][j] = 1

    #     for i in range(1, m):
    #         for j in range(1, n):
    #             dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    #     return dp[i][j]
    # # TC: O(m * n)
    # # SC: O(m * n)