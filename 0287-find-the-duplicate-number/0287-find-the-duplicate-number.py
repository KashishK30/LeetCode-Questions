class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    # FLOYD'S Tortoise and Hare Cycle Detection
        tortoise = nums[0]
        hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        finder = nums[0]
        while finder != tortoise:
            finder = nums[finder]
            tortoise = nums[tortoise]
        
        return finder