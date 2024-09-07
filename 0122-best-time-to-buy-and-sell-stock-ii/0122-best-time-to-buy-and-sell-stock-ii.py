class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Space Optimization
        n = len(prices)
        if n == 0:
            return 0
        
        ahead = [0, 0]
        curr = [0, 0]

        ahead[0] = ahead[1] = 0

        for i in range(n - 1, -1, -1):
            for j in range(2):
                profit = 0

                if j == 0: # Can buy
                    profit = max(-prices[i] + ahead[1], 0 + ahead[0])
                elif j == 1: # Can sell
                    profit = max(+prices[i] + ahead[0], 0 + ahead[1])
                curr[j] = profit
            ahead = curr
        return curr[0]
        # TC: O(n * 2)
        # SC: O(2)

        # # Tabulation
        # n = len(prices)
        # if n == 0:
        #     return 0
        
        # dp = [[-1 for _ in range(2)] for _ in range(n + 1)]

        # dp[0][0] = 0

        # for j in range(2):
        #     dp[n][j] = 0
        
        # profit = 0
        # for i in range(n - 1, -1, -1):
        #     for j in range(2):
        #         if j == 0:
        #             profit = max(-prices[i] + dp[i + 1][1], 0 + dp[i + 1][0])
        #         elif j == 1:
        #             profit = max(+prices[i] + dp[i + 1][0], 0 + dp[i + 1][1])
        #         dp[i][j] = profit

        # return dp[0][0]
        # # TC: O(n * 2)
        # # SC: O(n * 2)

        # # Memoization

        # n = len(prices)

        # if n == 0:
        #     return 0

        # dp = [[-1 for _ in range(2)] for _ in range(n)]

        # def memoization(ind, buy):
            
        #     if ind == n:
        #         return 0

        #     if dp[ind][buy] != -1:
        #         return dp[ind][buy]

        #     profit = 0

        #     if buy == 0:
        #         profit = max( -prices[ind] + memoization(ind + 1, 1), 
        #         0 + memoization(ind + 1, 0))
        #     elif buy == 1:
        #         profit = max( +prices[ind] + memoization(ind + 1, 0),
        #         0 + memoization(ind + 1, 1))

        #     dp[ind][buy] = profit
        #     return profit

        # return memoization(0, 0)

        # # TC: O(n * 2)
        # # SC: O(n * 2) + O(n)
