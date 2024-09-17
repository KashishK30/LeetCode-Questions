from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numbers = Counter(nums)
        
        for num, count in numbers.items():
            if (count > len(nums)//2):
                return num 