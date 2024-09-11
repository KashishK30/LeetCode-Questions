class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[-1 for _ in range(n)] for _ in range(n)]

        def memoization(i, j):
            if i + 1 == j:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            max_coins = 0

            for k in range(i + 1, j):
                coins = nums[i] * nums[k] * nums[j] + memoization(i, k) + memoization(k, j)
                max_coins = max(max_coins, coins)
                
            dp[i][j] = max_coins
            return dp[i][j]
        return memoization(0, n - 1)