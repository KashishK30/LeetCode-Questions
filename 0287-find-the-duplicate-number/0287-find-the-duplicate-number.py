class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    # FLOYD'S Tortoise and Hare Cycle Detection

        # Phase 1:
        # Finding the intersection point of the cycle
        # Initialize the tortoise and hare pointer to the first element
        tortoise = nums[0]
        hare = nums[0]

        # Move tortoise by one step and hare by two steps until they meet
        while True:
            # Tortoise move 1 step at a time
            tortoise = nums[tortoise]
            # Hare oves two step at a time
            hare = nums[nums[hare]]
            # If tortoise and hare meets, we found a cycle
            if tortoise == hare:
                break
        
        # Phase 2:
        # Finding the entrance of the cycle (duplicate numbers)
        # Initialize the finder pointer to the start of the array
        finder = nums[0]

        # Move both finder and tortoise 1 step at a time
        while finder != tortoise:
            # Move finder 1 step from start
            finder = nums[finder]
            # Move tortoise 1 step within cycle
            tortoise = nums[tortoise]
        
        # When finder meets tortise, it is at the start of the cycle
        # which corresponds to the duplicate number
        return finder