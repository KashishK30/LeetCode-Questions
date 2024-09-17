from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    # Boyer-Moore Voting Algorithm
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if candidate == num else -1)
        
        return candidate
    # TC: O(n)
    # SC: O(1)

    # # BRUTE FORCE
    #     numbers = Counter(nums)
        
    #     for num, count in numbers.items():
    #         if (count > len(nums)//2):
    #             return num 
    # # TC: O(n)
    # # SC: O(k)