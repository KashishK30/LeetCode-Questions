class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

        while l < r:
            mid = (l + r)// 2
            if self.canFinish(piles, h, mid):
                r = mid
            else:
                l = mid + 1
        return l

    def canFinish(self, piles, h, k):
        hours = 0
        for bananas in piles:
            hours += (bananas + k - 1)//k
        return hours <= h
        