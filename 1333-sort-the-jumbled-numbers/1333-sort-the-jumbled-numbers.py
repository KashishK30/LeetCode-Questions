class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map_value(num):
            mapped_str = ''.join(str(mapping[int(digit)]) for digit in str(num))
            return int(mapped_str)
        
        # Use the custom key for sorting
        sorted_nums = sorted(nums, key=map_value)
        return sorted_nums