class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    # OPTIMAL
        n = len(nums)

        if n == 0:
            return 0
        
        longest = 1

        # Create a set to store all unique numbers in the input list
        num_set = set()

        # Add all elements from set list to set for O(1) loop
        for i in range(n):
            num_set.add(nums[i])
        
        # Iterate through each numberr in the set
        for num in num_set:
            # Check if the current number is the start of the subsequence
            # i.e num - 1 should not be in the set
            if num - 1 not in num_set:
                # Initialize the count for current subsequence
                current_sequence_len = 1
                current_num = num

                # Find all consecutive numbers starting from num
                while current_num + 1 in num_set:
                    current_sequence_len += 1
                    current_num += 1
                
                longest = max(longest, current_sequence_len)
        return longest
    # TC: O(n) for inserting the elements into set
    # O(n) each no. in the set is checked at most once
    # Overall TC: O(n)
    # SC: O(n)

    # # BETTER
    #     n = len(nums)
    #     if n == 0:
    #         return 0

    #     nums.sort()
    #     last_smaller = float('-inf')
    #     count = 0
    #     longest = 1
        
    #     for i in range(n):
    #         if nums[i] == last_smaller + 1:
    #             count += 1
    #             last_smaller = nums[i]
    #         elif nums[i] != last_smaller:
    #             count = 1
    #             last_smaller = nums[i]
    #         longest = max(longest, count)
    #     return longest
    # # TC: O(n log n) + O(n) = sorting + 1 for loop
    # # SC: O(1)

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