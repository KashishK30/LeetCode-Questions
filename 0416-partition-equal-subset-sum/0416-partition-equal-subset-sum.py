class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ## SPACE OPTIMIZATION

        target = sum(nums) // 2
        n = len(nums)

        if sum(nums) % 2 != 0:
            return False
        
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[target]

        # TC: O(N*target), SC: O(target)

        ## TABULATION

        # n = len(nums)

        # if sum(nums) % 2 != 0:
        #     return False
        # target = sum(nums) // 2

        # dp = [[False] * (target + 1) for _ in range(n + 1)]
        
        # for i in range(n + 1):
        #     dp[i][0] =  True
            
        # for i in range(1, n + 1):
        #     for j in range(1, target + 1):
        #         if j >= nums[i - 1]:
        #             dp[i][j] = dp[i  - 1][j] or dp[i - 1][j - nums[i - 1]]
        #         else:
        #             dp[i][j] = dp[i - 1][j]
        # return dp[n][target]

        # # TC: O(n * target)