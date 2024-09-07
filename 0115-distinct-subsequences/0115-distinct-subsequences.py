class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Space Optimization

        m = len(s)
        n = len(t)
        prev = [0] * (n + 1)
        
        # Base Case: 
        prev[0] = 1 # Empty target string

        for i in range(1, m + 1):
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    prev[j] = prev[j - 1] + prev[j]
                         
        return prev[n]

        # # Tabulation

        # m = len(s)
        # n = len(t)
        # dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # # Base case: Empty target string matches with any source string
        # for i in range(m + 1):
        #     dp[i][0] = 1
        
        # # Base case: Empty source string match with no non_empty target list
        # for j in range(1, n + 1):
        #     dp[0][j] = 0

        # # Fill the dp table
        # for i in range(1, m + 1): # Staring from 1 to matches for non-empty string
        #     for j in range(1, n + 1):
        #         if s[i - 1] == t[j - 1]: 
        #             # if the char of souce and target string matches, take the sum of two cases:
        #             # 1. Include the char of 's' and keep matching
        #             # 2. Include the char of 's' in the match
        #             dp[i][j] =  dp[i - 1][j - 1] + dp[i - 1][j] 
        #         else:
        #             # if the source and target char does not match:
        #             # we can only exclude the current char of 's'
        #             dp[i][j] = dp[i - 1][j]
        # return dp[m][n]

        # # TC: O(m * n)
        # # SC: O(n)