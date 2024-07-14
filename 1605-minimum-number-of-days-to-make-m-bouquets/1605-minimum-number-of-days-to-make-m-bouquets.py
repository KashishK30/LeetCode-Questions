class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def canMake(days):
            bouquets = 0
            flowers = 0

            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

                if bouquets >= m:
                    return True
            return False
            
        n = len(bloomDay)
        if m * k > n:
            return -1
        
        left = min(bloomDay)
        right = max(bloomDay)
        ans = -1

        while left <= right:
            mid = (left + right)//2
            if canMake(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans