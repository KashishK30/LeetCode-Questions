class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # Tabulation
        n = len(arr)
        dp = [0] * (n + 1)

        for ind in range(n - 1, -1, -1):
            max_val = float('-inf')
            max_sum = 0
            for i in range(ind, min(ind + k, n)):
                max_val = max(max_val, arr[i])
                current_val = max_val * (i - ind + 1) + dp[i + 1]
                max_sum = max(max_sum, current_val)
            dp[ind] = max_sum
        return dp[0]

        # TC: O(n * k)
        # SC: O(n)


        # # Memeoization
        # n = len(arr)
        # dp = [-1] * (n)

        # def memoization(ind):
        #     if ind == n:
        #         return 0
            
        #     if dp[ind] != -1:
        #         return dp[ind]
            
        #     max_val = float('-inf')
        #     max_sum = 0
        #     for i in range(ind, min(ind + k, n)):
        #         max_val = max(max_val, arr[i])
        #         current_sum = (max_val * (i - ind + 1)) + memoization(i + 1)
        #         max_sum = max(current_sum, max_sum)
        #     dp[ind] = max_sum
        #     return dp[ind]

        # # TC: O(n * k)
        # # SC: O(n) + O(n) [Auxiliary stack space]

        return memoization(0)

        # # Recursion

        # def recursion(ind):
        #     if ind == len(arr):
        #         return 0
            
        #     max_val = float('-inf')
        #     max_sum = 0
        #     for i in range(ind, min(ind + k, len(arr))):
        #         max_val = max(max_val, arr[i])
        #         current_sum = max_val * (i - ind + 1) + recursion(i + 1)
        #         max_sum = max(max_sum, current_sum)

        #     return max_sum

        # return recursion(0)

        # # TC: Exponential

