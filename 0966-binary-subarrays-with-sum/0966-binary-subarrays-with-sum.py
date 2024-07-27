from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = 0
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        count = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - goal in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - goal]
            prefix_sum_count[prefix_sum] += 1

        return count