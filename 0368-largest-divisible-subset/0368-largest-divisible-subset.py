class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # # Step 1: Sort the array to make sure we only include divisible numbers in the correct order
        # nums.sort()
        # n = len(nums)

        # # dp[i] will store the largest subsequence that ends with nums[i]
        # dp = [[] for _ in range(n)]

        # # Initially each number is it's own subset
        # for ind in range(n):
        #     dp[ind] = [nums[ind]]

        # # Populate dp array with the largest divisible subset
        # for ind in range(1, n):
        #     for prev_ind in range(ind):
        #         # Check if nums[ind] is divisible by nums[prev_ind]
        #         if nums[ind] % nums[prev_ind] == 0:
        #             # If the subset ending at nums[prev_ind] is larger, update the subset ending at nums[ind]
        #             if len(dp[prev_ind]) + 1 > len(dp[ind]):
        #                 dp[ind] = dp[prev_ind] + [nums[ind]]

        # # Find the largest subset in dp
        # largest_subset = []
        # for subset in dp:
        #     if len(subset) > len(largest_subset):
        #         largest_subset = subset
        # return largest_subset

        # Algorithmic approach

        n = len(nums)

        # Sort the array in ascending order
        nums.sort()

        # Initialize dp and hash table with 1s
        dp = [1] * n
        hash_arr = list(range(n))

        # Iterate through array
        for ind in range(n):
            for prev_ind in range(ind):
                if nums[ind] % nums[prev_ind] == 0 and 1 + dp[prev_ind] > dp[ind]:
                    dp[ind] = 1 + dp[prev_ind]
                    hash_arr[ind] = prev_ind
        ans = -1
        last_ind = -1

        # Find the maximum length and it's correspong index

        for ind in range(n):
            if dp[ind] > ans:
                ans = dp[ind]
                last_ind = ind
        
        # Reconstruct thr divisible subset
        result = []

        while hash_arr[last_ind] != last_ind:
            result.append(nums[last_ind])
            last_ind = hash_arr[last_ind]
            
        result.append(nums[last_ind])

        result.reverse()
        return result

