class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # Optimal
        n = len(prices)
        min_before = float('inf')
        max_profit = 0

        for price in prices:
            min_before = min(price, min_before)
            max_profit = max(max_profit, price - min_before)
        return max_profit
    # TC: O(n) min and max take O(1) time complexity
    # SC: O(1)


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