class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # Optimal
        n = len(prices)
        min_before = prices[0]
        max_profit = 0

        for i in range(1, n):
            min_before = min(prices[i - 1], min_before)
            max_profit = max(max_profit, prices[i] - min_before)
        return max_profit
        


    # BRUTE FORCE

        # n = len(prices)
        # max_profit = 0

        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         profit = prices[j] - prices[i]
        #         max_profit = max(profit, max_profit)
        # return max_profit

    # # TC: O(n ^ 2)
    # # SC: O(1)