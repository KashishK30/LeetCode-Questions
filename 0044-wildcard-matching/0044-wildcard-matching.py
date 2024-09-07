class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Tabulation
        m = len(s)
        n = len(p)

        # Create a dp array of size (m + 1) * (n + 1)
        # dp[i][j] gives True if s[0: m] matches withp[0: n], False otherwise
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Base Case: Both string and pattern are empty, so they match
        dp[0][0] = True

        # Base Case: if string is empty, pattern can only match if it contains only "*"
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1] # "*" can match an empty string by acting as an empty string
            else:
                dp[0][j] = False # if there is a non "*" char in the pattern, it cannot match the empty string
        
        # Fill the table for i > 0 and j > 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Case1: if chars match or if pattern has "?" it can macth a single char
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                # Case 2: if charss do not match and pattern has "*", it can match the sequence of chars
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                # Case 3: if chars do not match and doesn't have "*' or "?"
                # it's already False
              
        return dp[m][n]
        # TC: O(m * n)
        # SC: O(m * n)

        # # Memoization

        # m = len(s)
        # n = len(p)

        # dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

        # def isAllStars(p, j):
        #     for k in range(j + 1):
        #         if p[k] != "*":
        #             return False
        #     return True
        
        # def memoization(i, j):

        #     if i < 0 and j < 0:
        #         return True
        #     if i < 0 :
        #         return isAllStars(p, j)
        #     if j < 0:
        #         return False
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     if s[i] == p[j] or p[j] == "?":
        #         dp[i][j] = memoization(i - 1, j - 1)
        #     elif p[j] == "*":
        #         dp[i][j] = memoization(i - 1, j) or memoization(i, j - 1)
        #     else:
        #         dp[i][j] = False

        #     return dp[i][j]
                    
        # return memoization(m - 1, n - 1)

        # # TC: O(m * n)
        # # SC: O(m * n) + O(m + n)
        
