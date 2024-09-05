class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)]

        for j in range(amount + 1):
            if j % coins[0] == 0:
                dp[0][j] = 1
        
        for i in range(1, n):
            for j in range(amount + 1):
                notTake = dp[i - 1][j]
                take = 0
                if coins[i] <= amount:
                    take = dp[i][j - coins[i]]
                dp[i][j] = take + notTake
        return dp[n - 1][amount]


        # n = len(coins)
        # dp = [[-1 for _ in range (amount + 1)] for _ in range(n)]

        # def Memoization(ind, target):
        #     if ind == 0:
        #         return 1 if target % coins[0] == 0 else 0

        #     if dp[ind][target] != -1:
        #         return dp[ind][target]
            
        #     notTake = Memoization(ind - 1, target)
        #     take = 0
        #     if coins[ind] <= target:
        #         take = Memoization(ind, target - coins[ind])
        #     return take + notTake
        # return Memoization(n - 1, amount)

        # def Recursion(ind, target):
        #     if ind == 0:
        #         if target % coins[0] == 0:
        #             return 1
        #         else:
        #             return 0
            
        #     notTake = Recursion(ind - 1, target)
        #     take = 0
        #     if coins[ind] <= target:
        #         take = Recursion(ind, target - coins[ind])
        #     result = take + notTake
        #     return result
        # return Recursion(len(coins) - 1, amount)
