from itertools import combinations
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Binary Search 
        n = len(nums)

        temp = [nums[0]]
        length = 1

        for i in range(1, n):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
                length += 1
            else:
                index = bisect.bisect_left(temp, nums[i])
                temp[index] = nums[i]

        return length

        # TC: O(n log n)
        # SC: O(1)

        # # Space Optimization

        # n = len(nums)
        # ahead = [0] * (n + 1)
        # curr = [0] * (n + 1)

        # for ind in range(n -1, -1, -1):
        #     for prev_ind in range(n - 1, -2, -1):
        #         notTake = 0 + ahead[prev_ind + 1]

        #         take = 0
        #         if prev_ind == -1 or nums[ind] > nums[prev_ind]:
        #             take = 1 + ahead[ind + 1]
                
        #         curr[prev_ind + 1] = max(take, notTake)
        #     ahead = curr
        # return ahead[0]

        # # TC: O(n * n)
        # # SC: O(n)

        # # Tabulation

        # # dp[i][j] = The length of LIS starting from index 'i',
        # # where the last index considered till now is 'j - 1'
        # n = len(nums)

        # # We use n + 1 indices to handle the base case of n o elements
        # dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        # # Fill the table from bottom-up
        # for ind in range(n - 1, -1, -1): # Iterate from last element to first
        #     for prev_ind in range(ind - 1, -2, -1): # Iterate from last element to index -1(prev_ind == -1: no previous element)
        #         # Option 1: Skip the current element
        #         notTake = 0 + dp[ind + 1][prev_ind + 1]

        #         # Option 2: take the current element
        #         take = 0

        #         # if current element > previous element or if it is the 1st element
        #         if nums[ind] > nums[prev_ind] or prev_ind == -1:
        #             take = 1 + dp[ind + 1][ind + 1] # curr_ind = ind + 1, prev_ind = ind

        #         dp[ind][prev_ind + 1] = max(take, notTake)
        # return dp[0][0] # curr_ind = 0, prev_ind = -1

        # # TC: O(n * n)
        # # SC: O(n * n) + O(n)

        # # Memoization

        # n = len(nums)
        # # Initialize the dp of size (n + 1) * (n + 1) and fill with -1
        # dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        # def memoization(ind, prev_ind):
        #     # Base case: If we have traversed all the elements no more subsequences can be formed
        #     if ind == n:
        #         return 0

        #     # if already computed, use it
        #     if dp[ind][prev_ind + 1] != -1: # prev + 1 to avoid accesing dp[ind][-1]
        #         return dp[ind][prev_ind + 1] 
            
        #     # Option 1: Do not take the current element
        #     notTake = 0 + memoization(ind + 1, prev_ind)

        #     # Take the current element 
        #     take = 0
        #     # If it is the first element or if it's larger than the current element
        #     if prev_ind == -1 or nums[ind] > nums[prev_ind]:
        #         take = 1 + memoization(ind + 1, ind)

        #     # Store the result in the dp array to avoid recomputation    
        #     dp[ind][prev_ind + 1] = max(take, notTake)

        #     return dp[ind][prev_ind + 1]
        
        # # Start recursion with index 0 and no previous element selected (Hence, previous index = -1)
        # return memoization(0, -1)

        # # TC: O(2 ** n)
        # # SC: O(n * n) + O(n)
