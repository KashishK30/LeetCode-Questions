class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n + 1)]

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                if buy == 0:
                    dp[ind][buy] = max(-prices[ind] + dp[ind + 1][1], 0 + dp[ind + 1][0])
                else:
                    dp[ind][buy] = max(+prices[ind] - fee + dp[ind + 1][0], 0 + dp[ind + 1][1])
        return dp[0][0]