class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        dp = [[float('-inf')] * n for _ in range(4)]

        dp[0][0] = a[0] * b[0]

        for j in range(1, n):
            dp[0][j] = max(dp[0][j - 1], a[0] * b[j])

        for k in range(1, 4):
            for j in range(k, n):
                dp[k][j] = max(dp[k][j - 1], dp[k - 1][j - 1] + a[k] * b[j])

        return dp[3][n - 1]

                    
