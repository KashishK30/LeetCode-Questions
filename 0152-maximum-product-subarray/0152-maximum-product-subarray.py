class Solution:
    def maxProduct(self, nums: List[int]) -> int:       
        if not nums:
            return 0

        max_prod = min_prod = result = nums[0]

        for i in range(1, len(nums)):
            current = nums[i]

            if current < 0:
                max_prod, min_prod = min_prod, max_prod
            
            max_prod = max(current, max_prod * current)
            min_prod = min(current, min_prod * current)

            result = max(max_prod, result)
        
        return result

        ## TC: O(n)
        ## SC: O(1)