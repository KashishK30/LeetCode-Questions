class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # Tabulation
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n + 2)]

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                if buy == 0:
                    dp[ind][buy] = max(-prices[ind] + dp[ind + 1][1], 0 + dp[ind + 1][0])
                else:
                    dp[ind][buy] = max(+prices[ind] + dp[ind + 2][0], 0 + dp[ind + 1][1])
        return dp[0][0]

    ## Memoization

    #     n = len(prices)

    #     if n == 0:
    #         return 0

    #     dp = [[-1 for _ in range(2)] for _ in range(n + 1)]

    #     def memoization(ind, buy):
    #         if ind >= n:
    #             return 0
            
    #         if dp[ind][buy] != -1:
    #             return dp[ind][buy]

    #         profit = 0
    #         if buy == 0:
    #             profit = max(-prices[ind] + memoization(ind + 1, 1), 0 + memoization(ind + 1, 0))
    #         else:
    #             profit = max(+prices[ind] + memoization(ind + 2, 0), 0 + memoization(ind + 1, 1))
            
    #         dp[ind][buy] = profit
    #         return profit
    #     return memoization(0, 0)

    # # TC: O(n * 2)
    # # SC: O(n * 2)
            
