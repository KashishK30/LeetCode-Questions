class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums)):
            farthest = max(farthest, nums[i] + i)

            if i == current_end:
                jumps += 1
                current_end = farthest

                if current_end >= n - 1:
                    break

        return jumps