class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ## Tabulation
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[m][n]

        ## TC: O(m * n)
        ## SC: O(min(m, n)) 

        ## Memoization
        # m = len(text1)
        # n = len(text2)
        # dp = [[-1] * (n + 1) for _ in range(m + 1)]

        # def lcs_memoization(text1, text2, m, n, dp):
        #     if m == 0 or n == 0:
        #         return 0

        #     if dp[m][n] != -1:
        #         return dp[m][n]

        #     if text1[m - 1] == text2[n - 1]:
        #         dp[m][n] = 1 + lcs_memoization(text1, text2, m - 1, n - 1, dp)
        #     else:
        #         dp[m][n] = max(lcs_memoization(text1, text2, m - 1, n, dp), lcs_memoization(text1, text2, m, n - 1, dp))
        #     return dp[m][n]
        
        # return lcs_memoization(text1, text2, m, n, dp)

        ## TC: O(m * n)
        ## SC: O(m * n)
            

        ## Recursion 

        # def lcs_recursive(text1, tex2, m, n):
        #     if m == 0 or n == 0:
        #         return 0
        #     elif text1[m - 1] == text2[n - 1]:
        #         return 1 + lcs_recursive(text1, text2, m - 1, n - 1)
        #     else:
        #         return max(lcs_recursive(text1, text2, m - 1, n), lcs_recursive(text1, text2, m, n - 1))

        # return lcs_recursive(text1, text2, len(text1), len(text2))
        ## TC: 2**(n + m)

        ## Brute Force
        # O(2^N)

