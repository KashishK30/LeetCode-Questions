class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totSum = sum(nums)

        if (totSum + target) % 2 != 0 or totSum < abs(target):
            return 0
        
        subset_sum = (totSum + target) // 2

        dp = [0] * (subset_sum + 1)
        dp[0] = 1

        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[subset_sum]
    
    