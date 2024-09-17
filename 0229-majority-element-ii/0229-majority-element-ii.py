from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count_num = Counter(nums)
        result = []

        for num, count in count_num.items():
            if count > n//3:
                result.append(num)
        return result
