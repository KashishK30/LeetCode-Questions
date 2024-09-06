class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        s1 = s
        s2 = s[::-1]
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        max_len_sub = dp[n][n]

        return n - max_len_sub



