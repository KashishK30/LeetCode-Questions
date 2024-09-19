class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # BETTER SOLUTION
        n = len(nums)
        num_to_index = {}
        result = []

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [i, num_to_index[complement]]
            num_to_index[num] = i

        return[-1, -1]
    # TC: O(n)
    # SC: O(1)

    # # BRUTE FORCE
    #     result = []
    #     n = len(nums)
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             if nums[i] + nums[j] == target:
    #                 result.append(i)
    #                 result.append(j)
    #     return result
    # # TC: O(n ^ 2)
    # # SC: O(1)