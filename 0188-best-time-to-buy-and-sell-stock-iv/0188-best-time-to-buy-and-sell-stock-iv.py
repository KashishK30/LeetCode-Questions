class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if n == 0 :
            return 0

        dp = [[[-1 for _ in range(k + 1)] for _ in range(2)] for _ in range(n + 1)]

        def memoization(ind, buy, cap):
            if ind == n or cap == 0:
                return 0

            if dp[ind][buy][cap] != -1:
                return dp[ind][buy][cap]
            
            profit = 0
            if buy == 0: # Can buy : max(buy, not buy)
                profit = max(-prices[ind] + memoization(ind + 1, 1, cap), 0 + memoization(ind + 1, 0, cap))
            elif buy == 1: # Can sell: max(sell, not sell)
                profit = max(+prices[ind] + memoization(ind + 1, 0, cap - 1), 0 + memoization(ind + 1, 1, cap))
            else:
                return 0
            dp[ind][buy][cap] = profit

            return profit

        return memoization(0, 0, k)

        # TC: 


        