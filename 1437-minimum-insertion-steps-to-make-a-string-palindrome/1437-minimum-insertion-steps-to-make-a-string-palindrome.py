class Solution:
    def minInsertions(self, s: str) -> int:
        # Space Optimization
        n = len(s)
        s1 = s
        s2 = s[::-1]

        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr[:]
        max_common_len_sub = prev[n]

        return n - max_common_len_sub

        # # Tabulation

        # n = len(s)
        # s1 = s
        # s2 = s[::-1]
        # dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        
        # for i in range(1, n + 1):
        #     for j in range(1, n + 1):
        #         if s1[i - 1] == s2[j - 1]:
        #             dp[i][j] = 1 + dp[i - 1][j - 1]
        #         else:
        #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # max_len_sub = dp[n][n]

        # return n - max_len_sub

        # # TC: O(n * n)
        # # SC: O(n * n)



