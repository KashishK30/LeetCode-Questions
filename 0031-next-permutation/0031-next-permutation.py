class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return

        k = n - 2
        # Step 1: Find the largest index k such that nums[k] < nums[k + 1]
        while k >= 0 and nums[k] >= nums[k + 1]:
            k -= 1
        
        if k >= 0:
            # Step 2: Find the largest index l greater than k such that nums[k] < nums[l]
            l = n - 1
            while nums[k] >= nums[l]:
                l -= 1

            # Step 3: Swap the values of nums[k] and nums[l]
            nums[k], nums[l] = nums[l], nums[k]

        # Step 4: Reverse the sequence from sequence k + 1 to end
        nums[k + 1:] = reversed(nums[k + 1:])
    
        return nums

