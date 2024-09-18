class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert integers to strings
        nums_str = list(map(str, nums))
        
        # Custom sort key: we use x*10 as a trick to ensure proper sorting
        nums_str.sort(key=lambda x: x*10, reverse=True)
        
        # Join sorted numbers to form the largest number
        largest_num = ''.join(nums_str)
        
        # Edge case: if the largest number starts with '0', return '0'
        if largest_num[0] == '0':
            return '0'
        
        return largest_num