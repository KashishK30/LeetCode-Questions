class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Space Optimization

        n = len(prices)
        ahead = [0, 0]
        curr = [0, 0]

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                if buy == 0:
                    curr[buy] = max(- prices[ind] + ahead[1], 0 + ahead[0])
                else:
                    curr[buy] = max(+ prices[ind] - fee + ahead[0], 0 + ahead[1])
            ahead = curr[:]
        return ahead[0]

        # TC: O(n * 2)
        # SC: O(2)

        # # Tabulation

        # n = len(prices)
        # dp = [[0 for _ in range(2)] for _ in range(n + 1)]

        # for ind in range(n - 1, -1, -1):
        #     for buy in range(2):
        #         if buy == 0:
        #             dp[ind][buy] = max(-prices[ind] + dp[ind + 1][1], 0 + dp[ind + 1][0])
        #         else:
        #             dp[ind][buy] = max(+prices[ind] - fee + dp[ind + 1][0], 0 + dp[ind + 1][1])
        # return dp[0][0]

        # # TC: O(n * 2)
        # # SC: O(n * 2)