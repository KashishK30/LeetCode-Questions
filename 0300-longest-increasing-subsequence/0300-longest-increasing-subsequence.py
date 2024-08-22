from itertools import combinations

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ## Brute Force (Exponential time)
        # Generate all susequesnces of the array then filter out those who are strictly increasing
        # TC: O(N^2)

        ## Recursive Solution
        # not take = f(ind + 1, prev_inddex)
        # take = 1 + f(ind + 1, ind)
        # return max(take, not_take)

        # Dynamic Programming
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

        ## Memoization

        # n = len(nums)
        # dp = [[-1] * (n + 1) for _ in range(n)]

        # def helper(ind, pre_ind):
        #     if ind == n:
        #         return 0
            
        #     if dp[ind][pre_ind + 1] != -1:
        #         return dp[ind][pre_ind + 1]

        #     not_take = helper(ind + 1, pre_ind)

        #     take = 0
        #     if pre_ind == -1 or nums[ind] > nums[pre_ind]:
        #         take = 1 + helper(ind + 1, ind)
            
        #     dp[ind][pre_ind + 1] = max(take, not_take)

        #     return dp[ind][pre_ind + 1]
        # return helper(0, -1)

            


        ## Recursion

        # def lengthOfLISRecursive(nums, ind, pre_index):
        #     if ind >= len(nums):
        #         return 0
            
        #     not_take = lengthOfLISRecursive(nums, ind + 1, pre_index)

        #     take = 0
        #     if pre_index == -1 or nums[ind] > nums[pre_index]:
        #         take = 1 + lengthOfLISRecursive(nums, ind + 1, ind)
        #     return max(take, not_take)

        # return lengthOfLISRecursive(nums, 0, -1)
            
        ## Brute Force

        # def is_increasing_subsequence(sub_seq):
        #     n = len(sub_seq)
        #     return all(sub_seq[i] < sub_seq[i + 1] for i in range(n - 1))
        
        # longest = 0
        # for length in range(1, len(nums) + 1):
        #     for sub_seq in combinations(nums, length):
        #         if is_increasing_subsequence(sub_seq):
        #             longest = max(longest, len(sub_seq))
        # return longest

        

