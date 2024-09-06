class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Del all the chars from the word1 which are not part of the longest common subsequence
        #  n - lcs
        # Add all the chars to the lcs which are not part of the word2
        # m - lcs
        # Total = (n - lcs) + (m - lcs) = (n + m) - (2 * lcs)

        # Space Optimization

        m = len(word1)
        n = len(word2)

        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr[:]
        lcs = prev[n]

        return (m + n) - (2 * lcs)


        # # Tabulation

        # m = len(word1)
        # n = len(word2)

        # dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if word1[i - 1] == word2[j - 1]:
        #             dp[i][j] = 1 + dp[i - 1][j - 1]
        #         else:
        #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # lcs = dp[m][n]

        # return (n + m) - (2 * lcs)

        # # TC: O(m * n)
        # # SC: O(m * n)