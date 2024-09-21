class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    # BETTER
        n = len(nums)
        if n == 0:
            return 0

        nums.sort()
        last_smaller = float('-inf')
        count = 0
        longest = 1
        
        for i in range(n):
            if nums[i] == last_smaller + 1:
                count += 1
                last_smaller = nums[i]
            elif nums[i] != last_smaller:
                count = 1
                last_smaller = nums[i]
            longest = max(longest, count)
        return longest
    # TC: O(n log n) + O(n) = sorting + 1 for loop
    # SC: O(1)

    # BRUTE FORCE
        # n = len(nums)
        # longest  = 1

        # def linearSearch(nums, num):
        #     for i in range(n):
        #         if nums[i] == num:
        #             return True
        #     return False

        # for i in range(n):
        #     x = nums[i]
        #     count = 1
        #     while linearSearch(nums, x + 1):
        #         x = x + 1
        #         count += 1
        #     longest = max(count, longest)
              
        # return longest  
    # TC: O(N ^ 2)
    # SC: O(1)