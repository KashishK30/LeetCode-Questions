class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Optimal Solution
        # KADANE'S Algorithm
        # n = len(nums)

        # max_sum = float('-inf')
        # sum_arr = 0

        # for i in range(n):
        #     sum_arr = max(sum_arr + nums[i], nums[i])
        #     max_sum = max(sum_arr, max_sum)
        # return max_sum

        # TC: O(n)
        # SC: O(1)

        # DP Solution
        n = len(nums)
        dp = [0] * n

        dp[0] = nums[0]

        max_sum = dp[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            max_sum = max(dp[i], max_sum)
        return max_sum

        # TC: O(n)
        # SC: O(n)

        # Better Approach
        # n = len(nums)

        # max_sum = float('-inf')
        # for i in range(n):
        #     sum_arr = 0
        #     for j in range(i, n):
        #         sum_arr += nums[j]
        #         max_sum = max(max_sum, sum_arr)
        # return max_sum

        # TC: O(n^ 2)
        # SC: O(1)

        # # Brute Force
        # n = len(nums)

        # max_sum = float('-inf')
        # for i in range(n):
        #     for j in range(i, n):
        #         sum_arr = 0
        #         for k in range(i, j + 1):
        #             sum_arr += nums[k]
        #         max_sum = max(max_sum, sum_arr)
        # return max_sum

        # # TC: O(n ^ 3)
        # # SC: O(1)