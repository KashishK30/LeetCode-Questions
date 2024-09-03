class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Space Optimization
        # n = len(nums)
        # total_sum = sum(nums)

        # if total_sum % 2 != 0:
        #     return False
        
        # target = total_sum // 2

        # prev = [False] * (target + 1)

        # prev[0] = True

        # if nums[0] <= target:
        #     prev[nums[0]] = True
        
        # for i in range(1, n):
        #     curr = [False] * (target + 1)
        #     curr[0] = True
        #     for j in range(1, target + 1):
        #         notTake = prev[j]
        #         take = False
        #         if nums[i] <= j:
        #             take = prev[j - nums[i]]
        #         curr[j] = take or notTake
        #     prev = curr
        
        # return prev[target]

        # TC: O(n * target) + O(n)
        # SC: O(target)

        # # Tabulation
        n = len(nums)
        total_sum = sum(nums)
        
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2

        dp = [[False for _ in range(target + 1)] for _ in range(n)]

        for i in range(1, n):
            dp[i][0] = True

        if nums[0] <= target:
            dp[0][nums[0]] = True
        
        for i in range(1, n):
            for j in range(1, target + 1):
                notTake = dp[i - 1][j]

                take = False
                if nums[i] <= j:
                    take = dp[i - 1][j - nums[i]]
                dp[i][j] = take or notTake
        
        return dp[n - 1][target]

        # # TC: O(n * target) + O(n)
        # # SC: O(n * target)

        # # Memoization
        # n = len(nums)
        # total_sum = sum(nums)
        
        # dp = [[-1 for _ in range(total_sum + 1)] for _ in range(n)]

        # def memoization(ind, target):
        #     # Base cases
        #     if target == 0:
        #         return True
            
        #     if ind == 0:
        #         return nums[ind] == 0

        #     if dp[ind][target] != -1:
        #         return dp[ind][target]
            
        #     notTake = memoization(ind - 1, target)
        #     take = False
        #     if nums[ind] <= target:
        #         take =  memoization(ind - 1, target - nums[ind])

        #     dp[ind][target] = take or notTake
        #     return dp[ind][target]

        # if total_sum % 2 != 0:
        #     return False
        
        # target = total_sum // 2
        # return memoization(n - 1, target)

        # # TC: O(n * target) + O(n)
        # # SC: O(n * target) + O(n)


        # # Recursion
        # def Recursion(ind, target):
        #     # Base cases
        #     if target == 0:
        #         return True
        #     if ind == 0:
        #         return nums[0] == target
            
        #     # Exclude the current element
        #     notTake = Recursion(ind - 1, target)

        #     take = False
        #     if nums[ind] <= target:
        #         take = Recursion(ind - 1, target - nums[ind])
            
        #     return take or notTake

        # total_sum = sum(nums)
        # if total_sum % 2 != 0:
        #     return False
        
        # target = total_sum // 2
        # n = len(nums)
        # return Recursion(n - 1, target)

        # # TC: O(2^n) + O(n)
        # # SC: O(n)