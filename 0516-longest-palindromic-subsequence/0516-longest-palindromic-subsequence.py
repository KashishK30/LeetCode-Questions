class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Space Optimization

        a = s
        b = s[::-1]
        n = len(s)

        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if a[i - 1] == b[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr[:]
        return prev[n]

        # # Tabulation

        # a = s
        # b = s[::-1] 
        
        # def lcs(s1, s2):
        #     m = len(s1)
        #     n = len(s2)

        #     dp = [[-1] * (n + 1) for _ in range(m + 1)]

        #     for i in range(m + 1):
        #         dp[i][0] = 0
        #     for j in range(n + 1):
        #         dp[0][j] = 0

        #     for i in range(1, m + 1):
        #         for j in range(1, n + 1):
        #             if s1[i - 1] == s2[j - 1]:
        #                 dp[i][j] = 1 + dp[i - 1][j - 1]
        #             else:
        #                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                        
        #     return dp[m][n]
        
        # return lcs(a, b)

        # # TC: O(N * N)
        # # SC: O(N * N)