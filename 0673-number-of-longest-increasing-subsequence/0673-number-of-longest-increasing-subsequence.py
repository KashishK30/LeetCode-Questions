class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        dp = [1] * n
        count = [1] * n

        for ind in range(n):
            for prev_ind in range(ind):
                if nums[prev_ind] < nums[ind]:
                    if dp[prev_ind] + 1 > dp[ind]:
                        dp[ind] = 1 + dp[prev_ind]
                        count[ind] = count[prev_ind] # Inherit
                    elif dp[prev_ind] + 1 == dp[ind]:
                        count[ind] += count[prev_ind] # Increase the count
        max_length = max(dp)

        max_count = sum(count[ind] for ind in range(n) if dp[ind] == max_length)

        return max_count