class Solution:   
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # Space Optimization
        # dp = [float('inf')] * (amount + 1)
        # dp[0] = 0 # 0 coins are needed to make amount 0

        # # Fill the dp table
        # for i in range(1, amount + 1):
        #     for coin in coins:
        #         if coin <= i:
        #             dp[i] = min(dp[i], dp[i - coin] + 1)
        # return dp[amount] if dp[amount] != float('inf') else -1

        # # TC: O(N * T)
        # # SC: O(T)

        # Tabulation
        n = len(coins)
        # Create a 2D DP array with dimensions (len(coins) + 1) * (amount + 1)
        dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
        
        # Base case: 0 amount requires 0 coins
        for i in range(n + 1):
            dp[i][0] = 0
        
        for i in range(n + 1):
            for j in range(amount + 1):
                dp[i][j] = dp[i - 1][j] # When we do not take the ith coin
                
                # Case when we use the ith coin only if current value <= current amount
                if coins[i - 1] <= j:
                    dp[i][j] = min(dp[i][j] ,dp[i][j - coins[i - 1]] + 1)
        
        return dp[n][amount] if dp[n][amount] != float('inf') else -1

        # TC: O(N * T)
        # SC: O(N * T)
                
        # # Memoization
        # def coinChange(ind: int, target: int, dp: List[List[int]]) -> int:
        #    Base Cases
        #     if target == 0:
        #         return 0
        #     if ind == 0:
        #         return float('inf') if target % coins[0] != 0 else target //coins[ind]

        #     # Check if result is already computed
        #     if dp[ind][target] != -1:
        #         return dp[ind][target]
            
        #     # Recursive Cases
        #     notTake = coinChange(ind - 1, target, dp) # Exclude the current coin
        #     take = inf('float')
        #     if target <= coins[ind]:
        #         take = 1 + coinChange(ind, target - coins[ind], dp)
            
        #     dp[ind][target] = min(take, notTake)
        #     return dp[ind][target]
        
        # n = len(coins)   
        # dp = [[-1] * (amount + 1) for _ in range(n)]
        # result = coinChange(n - 1, amount, dp)
        # return result if result != float('inf') else -1

        # # TC: O(N * T)
        # # SC: O(N * T) + O(N) recursive stack space

        # # Recursion
        # def coinChangeRecursive(ind: int, target: int) -> int:
        #     # Base Case
        #     if target == 0:
        #         return 0
        #     if ind == 0:
        #         return float('inf') if target % coins[0] != 0 else target // coins[0]

        #     # Recursive cases

        #     notTake = 0 + coinChangeRecursive(ind - 1, target) # Exclude the current coin

        #     take = float('inf')
        #     if coins[ind] <= target:
        #         take = 1 + coinChangeRecursive(ind, target - coins[ind]) # Include the current coin

        #     return min(take, notTake)

        # result = coinChangeRecursive(len(coins) - 1, amount)
        # return result if result != float('inf') else -1

        # # TC: Exponential O(2^n) due to overlapping problem
        # # SC: O(n) Maximum depth of resursion



