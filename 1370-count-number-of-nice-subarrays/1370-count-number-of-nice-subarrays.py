class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def count_at_most(k):
            odd_numbers = 0
            left = 0
            count = 0

            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd_numbers += 1
                while odd_numbers > k:
                    if nums[left] % 2 == 1:
                        odd_numbers -= 1
                    left += 1
                count += right - left + 1
            return count

        return count_at_most(k) - count_at_most(k - 1)