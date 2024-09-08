class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Tabulation

        n = len(prices)
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]

        # Base cases are already covered as the dp is initialized to 0
      
        for i in range(n - 1, -1, -1):
            for j in range(2):
                for k in range(1, 3):
                    if j == 0:
                        dp[i][j][k] = max(-prices[i] + dp[i + 1][1][k], 0 + dp[i + 1][0][k])
                    elif j == 1:
                        dp[i][j][k] = max(+prices[i] + dp[i + 1][0][k - 1], 0 + dp[i + 1][1][k])

        return dp[0][0][2]



        # # Memoization

        # n = len(prices)
        # # Create a 3D DP table with dimentions (n * 2 * 3) and initializa it with -1
        # dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]

        # # Recursive funtion to find the maximum profit
        # def memoization(ind, buy, cap):
        #     # if we have reached the end of the array or used up all transactions, return zero profit
        #     if ind == n or cap == 0:
        #         return 0

        #     # if the result is already computed, return it
        #     if dp[ind][buy][cap] != -1:
        #         return dp[ind][buy][cap]
            
        #     profit = 0

        #     if buy == 0:
        #         # We can buy the stock
        #         profit = max(0 + memoization(ind + 1, 0, cap), -prices[ind] + memoization(ind + 1, 1, cap))
        #     elif buy == 1:
        #         # We can buy the stock
        #         profit = max(0 + memoization(ind + 1, 1, cap), prices[ind] + memoization(ind + 1, 0, cap - 1))

        #     dp[ind][buy][cap] = profit
        #     return dp[ind][buy][cap]
        
        # return memoization(0, 0, 2)
        # # TC: O(n * 2 * 3)
        # # SC: O(n * 2 * 3) + O(n)


