class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
    # OPTIMAL SOLUTION

        # count: to store the no. of subarrays whose is equals to k
        # current_sum: to store the running prefix sum
        # prefix_sum: a hashmap (dictionary) to store the frequency of each prefix sum
        n = len(nums)
        count = 0
        current_sum = 0
        prefix_sums = {0: 1} # We start with prefix_sums[0] = 1, to handle subarray starting from index 0

        for num in nums:
            # Add the current no. to the running prefix sum
            current_sum += num
        
            # Check if there is a subarray that sums to k
            # If (current - sum) exist in the prefix_sums hashmap,
            # it means we have found a subarray whose su is k
            if current_sum - k in prefix_sums:
                count += prefix_sums[current_sum - k]

            # Update the prex_sums hashmap
            # If current_sum has been seen before, increment it's count
            # Otherwise initialize it's count to 1
            if current_sum in prefix_sums:
                prefix_sums[current_sum] += 1
            else:
                prefix_sums[current_sum] = 1

        # Return the total count of subarray whose sum equals to k
        return count        

    # TC: O(n)
    # SC: O(n) in the worst case scenariowo would insert all array elements prefix sums into the hashmap

    # # BRUTE FORCE
    #     n = len(nums)
    #     count = 0
        
    #     for i in range(n):
    #         sum_subarr = 0
    #         for j in range(i, n):
    #             sum_subarr += nums[j]
    #             if sum_subarr == k:
    #                 count += 1
    #     return count
    # # TC: O(n ^ 2)
    # # SC: O(1)