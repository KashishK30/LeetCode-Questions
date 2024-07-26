class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        deq = deque()
        result = []

        for i in range(len(nums)):
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)

            if deq[0] == i - k:
                deq.popleft()

            if i >= k - 1:
                result.append(nums[deq[0]])
        
        return result
        
