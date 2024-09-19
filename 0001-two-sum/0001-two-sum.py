class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # BRUTE FORCE
        result = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
        return result
    # TC: O(n ^ 2)
    # SC: O(1)