class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # # BETTER SOLUTION (Optimal for yes or no question, without printing index)
    #     # Step 1: Store the original indices along with the values
    #     indexed_arr = list(enumerate(nums))

    #     # Step 2: Sort based on the values (not indices)
    #     indexed_arr.sort(key = lambda x: x[1])

    #     # Step 3: Two-pointers technique
    #     n = len(nums)
    #     l = 0
    #     r = len(nums) - 1

    #     while l < r:
    #         current_sum = indexed_arr[l][1] + indexed_arr[r][1]

    #         if current_sum == target:
    #             return [indexed_arr[l][0], indexed_arr[r][0]]
            
    #         elif current_sum > target:
    #             r -= 1
            
    #         else:
    #             l += 1
            
    #     return [-1, -1]
    # # TC: O(n * log n)
    # # SC: O(n)

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