class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # Space Optimization

        n = len(prices)
        
        ahead = [[0] * (k + 1) for _ in range(2)]
        curr = [[0] * (k + 1) for _ in range(2)]

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, k + 1):
                    if buy == 0:
                        curr[buy][cap] = max(-prices[ind] + ahead[1][cap], 0 + ahead[0][cap])
                    else:
                        curr[buy][cap] = max( + prices[ind] + ahead[0][cap - 1], 0 + ahead[1][cap])
                ahead = curr[:]
        return ahead[0][k]
        # TC: O(k * 2)
        # SC: O(k * 2)

        # # Tabulation

        # n = len(prices)

        # if n == 0:
        #     return 0

        # dp = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(n + 1)]

        # for ind in range(n - 1, -1, -1):
        #     for buy in range(2):
        #         for cap in range(1, k + 1):
        #             if buy == 0:
        #                 dp[ind][buy][cap] = max(-prices[ind] + dp[ind + 1][1][cap], 0 + dp[ind + 1][0][cap])
        #             else:
        #                 dp[ind][buy][cap] = max(+prices[ind] + dp[ind + 1][0][cap - 1], 0 + dp[ind + 1][1][cap])
        # return dp[0][0][k]

        # # TC: O(n * 2 * k)
        # # SC: O(n * 2 * k)

        # # Memoization

        # n = len(prices)

        # if n == 0 :
        #     return 0

        # dp = [[[-1 for _ in range(k + 1)] for _ in range(2)] for _ in range(n + 1)]

        # def memoization(ind, buy, cap):
        #     if ind == n or cap == 0:
        #         return 0

        #     if dp[ind][buy][cap] != -1:
        #         return dp[ind][buy][cap]
            
        #     profit = 0
        #     if buy == 0: # Can buy : max(buy, not buy)
        #         profit = max(-prices[ind] + memoization(ind + 1, 1, cap), 0 + memoization(ind + 1, 0, cap))
        #     elif buy == 1: # Can sell: max(sell, not sell)
        #         profit = max(+prices[ind] + memoization(ind + 1, 0, cap - 1), 0 + memoization(ind + 1, 1, cap))
        #     else:
        #         return 0
        #     dp[ind][buy][cap] = profit

        #     return profit

        # return memoization(0, 0, k)

        # # TC: O(k * 2 * n)
        # # SC: O(k * 2 * n) + O(n)




        