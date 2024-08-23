class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ## Space Optimization
        m = len(word1)
        n = len(word2)

        cur = [0 for _ in range(n + 1)]
        prev = [j for j in  range(n + 1)]

        for i in range(1, m + 1):
            cur[0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    cur[j] = prev[j - 1]
                else:
                    cur[j] = 1 + min(prev[j - 1], prev[j], cur[j - 1])
            prev, cur = cur, prev

        return prev[n]

        ## TC: O(m * n)
        ## SC: O(n)

        ## Tabulation

        # m = len(word1)
        # n = len(word2)

        # dp = [[0 for _ in  range(n + 1)] for _ in range(m + 1)]

        # for i in range(m + 1):
        #     dp[i][0] = i
        # for j in  range(n + 1):
        #     dp[0][j] = j
        
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if word1[i - 1] == word2[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1]
        #         else:
        #             insert = 1 + dp[i][j - 1]
        #             delete = 1 + dp[i - 1][j]
        #             replace = 1 + dp[i - 1][j - 1]
        #             dp[i][j] = min(insert, delete, replace)
        # return dp[m][n]

        ## TC: O(m * n)
        ## SC: O( m * n)

        ## Memoization

        # m = len(word1)
        # n = len(word2)

        # dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

        # def helper(i, j):
        #     if i < 0:
        #         return j + 1
        #     if j < 0:
        #         return i + 1

        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     if word1[i] == word2[j]:
        #         dp[i][j] = helper(i - 1, j - 1)
        #     else:
        #         insert_char = 1 + helper(i, j - 1) # Insert
        #         delete_char = 1 + helper(i - 1, j) # Delete
        #         replace_char = 1 + helper(i - 1, j - 1) # Replace

        #         dp[i][j] = min(insert_char, delete_char, replace_char)
            
        #     return dp[i][j]

        # return helper(m - 1, n - 1)

        # ## TC: O(m * n)
        # ## SC: O(m * n) + O(m + n) for recursion stack