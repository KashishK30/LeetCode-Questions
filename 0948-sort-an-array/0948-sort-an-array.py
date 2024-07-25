class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

    def merge_sort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left_half = self.merge_sort(nums[:mid])
        right_half = self.merge_sort(nums[mid:])

        return self.merge(left_half, right_half)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        left_index = 0
        right_index = 0
        sorted_array = []

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                sorted_array.append(left[left_index])
                left_index += 1
            else:
                sorted_array.append(right[right_index])
                right_index += 1
        sorted_array.extend(left[left_index:])
        sorted_array.extend(right[right_index:])

        return sorted_array
