class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_len = 0
        left = 0
        count_0 = 0
        
        for r in range(n):
            if nums[r] == 0:
                count_0 += 1
            
            while count_0 > k:
                if nums[left] == 0:
                    count_0 -= 1
                left += 1
            
            max_len = max(max_len, r - left + 1)
        
        return max_len

        