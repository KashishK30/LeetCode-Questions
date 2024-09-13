class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        palindrome = [[False] * n for _ in range(n)]

        for i in range(n):
            palindrome[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] :
                    if length == 2:
                        palindrome[i][j] = True
                    else:
                        palindrome[i][j] = palindrome[i + 1][j - 1]

        dp = [float('inf')] * n
        for i in range(n):
            if palindrome[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if palindrome[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        return dp[n - 1]

        # # Tabulation
        # n = len(s)
        
        # # Initialize dp array
        # dp = [float('inf')] * (n + 1)
        # dp[0] = -1  # No cuts needed before the start
        
        # def palindrome(i, j):
        #     # Check if s[i:j+1] is a palindrome
        #     while i < j:
        #         if s[i] != s[j]:
        #             return False
        #         i += 1
        #         j -= 1
        #     return True
        
        # # Compute minimum cuts for all substrings
        # for end_ind in range(n):
        #     for start_ind in range(end_ind + 1):
        #         if palindrome(start_ind, end_ind):
        #             dp[end_ind + 1] = min(dp[end_ind + 1], dp[start_ind] + 1)
        
        # return dp[n]  # Return the minimum cuts for the whole string

        # TC: O(n * n)
        # SC: O(n)

        # # Memoization
        # n = len(s)

        # dp = [-1] * (n + 1)

        # def palindrome(i, j):
        #     while i < j:
        #         if s[i] != s[j]:
        #             return False
        #         i += 1
        #         j -= 1
        #     return True

        # def memoization(start_ind):
        #     if start_ind == n:
        #         return 0
            
        #     if dp[start_ind] != -1:
        #         return dp[start_ind]

        #     min_cost = float('inf')
            
        #     for end_ind in range(start_ind, n):
        #         if palindrome(start_ind, end_ind):
        #             cost = 1 + memoization(end_ind + 1)
        #             min_cost = min(min_cost, cost)

        #     dp[start_ind] = min_cost
        #     return dp[start_ind]

        # return memoization(0) - 1

        # # TC: O(n * n)
        # # SC: O(n) + O(n)


        # # Recursion
        # n = len(s)
        
        # def palindrome(i, j):
        #     while i < j:
        #         if s[i] != s[j]:
        #             return False
        #         i += 1
        #         j -= 1
        #     return True

        # def recursion(start_ind, n):
        #     if start_ind == n:
        #         return 0

        #     min_cost = float('inf')

        #     for end_ind in range(start_ind, n):
        #         if palindrome(start_ind, end_ind):
        #             cost = 1 + recursion(end_ind + 1, n)
        #             min_cost = min(cost, min_cost)
        #     return min_cost
        
        # return recursion(0, n) - 1

        # # TC: Exponential