class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 0:
            return 0

        dp = [[-1 for _ in range(2)] for _ in range(n + 1)]

        def memoization(ind, buy):
            if ind >= n:
                return 0
            
            if dp[ind][buy] != -1:
                return dp[ind][buy]

            profit = 0
            if buy == 0:
                profit = max(-prices[ind] + memoization(ind + 1, 1), 0 + memoization(ind + 1, 0))
            else:
                profit = max(+prices[ind] + memoization(ind + 2, 0), 0 + memoization(ind + 1, 1))
            
            dp[ind][buy] = profit
            return profit
        return memoization(0, 0)
            
