class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    # INSERTION SORT
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key

        return nums


    # # SELECTION SORT

    #     n = len(nums)
    #     for i in range(n):
    #         min_ind = i
    #         for j in range(i + 1, n):
    #             if nums[j] < nums[min_ind]:
    #                 min_ind = j

    #         nums[i], nums[min_ind] = nums[min_ind], nums[i]
    #     return nums

    # # TC: O(n ^ 2)
    # # SC: O(1)

    # # BUBBLE SORT

    #     n = len(nums)
    #     for i in range(n):
    #         for j in range(n - i - 1):
    #             if nums[j] > nums[j + 1]:
    #                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
    #     return nums

    # # TC: O(n ^ 2)
    # # SC: O(1)

    # # Brute Force

        # n = len(nums)
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         if nums[i] > nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]
        # return nums

    # # TC: O(n ^ 2)
    # # SC: O(1)
