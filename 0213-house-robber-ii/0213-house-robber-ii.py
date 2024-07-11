class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        def linear_rob(arr):
            if not arr:
                return 0
            if len(arr) == 1:
                return arr[0]

            prev2 = arr[0]
            prev1 = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                current = max(prev1, prev2 + arr[i])
                prev2 = prev1
                prev1 = current
            return prev1

        case1 = linear_rob(nums[1:])
        case2 = linear_rob(nums[:-1])

        return max(case1, case2)
